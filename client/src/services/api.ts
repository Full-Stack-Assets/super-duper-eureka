import type {
  AlertsResponse,
  BenchmarksResponse,
  DashboardSummary,
  IngestionQueueItem,
  IngestionQueueResponse,
  InventoryLevel,
  MarginDrilldown,
  MarginGapResponse,
  PriceTrendPoint,
  ReorderResponse,
  ShrinkageResponse,
  VendorResponse,
} from '@/data/mockData';

export interface MarginGapParams {
  location?: string;
  dateFrom?: string;
  dateTo?: string;
  category?: string;
}

export interface InvoiceUploadResponse {
  message?: string;
  jobId?: string;
  fileName?: string;
  status?: string;
  parsingStatus?: string;
  state?: string;
  vendor?: string;
  [key: string]: unknown;
}

export interface InvoiceJobStatusResponse {
  id?: string;
  jobId?: string;
  status?: IngestionQueueItem['status'] | string;
  parsingStatus?: IngestionQueueItem['status'] | string;
  state?: IngestionQueueItem['status'] | string;
  fileName?: string;
  uploadedAt?: string;
  location?: string;
  vendor?: string;
  documentType?: string;
  detail?: string;
  message?: string;
  source?: IngestionQueueItem['source'] | string;
}

const buildQuery = (params?: object) => {
  const search = new URLSearchParams();
  Object.entries((params ?? {}) as Record<string, unknown>).forEach(([key, value]) => {
    if (value !== undefined && value !== null && value !== '') {
      search.set(key, String(value));
    }
  });
  const query = search.toString();
  return query ? `?${query}` : '';
};

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(path, {
    headers: {
      'Content-Type': 'application/json',
      ...(init?.headers ?? {}),
    },
    ...init,
  });

  if (!response.ok) {
    throw new Error(`API request failed: ${response.status} ${response.statusText}`);
  }

  return response.json() as Promise<T>;
}

async function requestFirstAvailable<T>(paths: string[], init?: RequestInit): Promise<T> {
  let lastError: unknown;

  for (const path of paths) {
    try {
      return await request<T>(path, init);
    } catch (error) {
      lastError = error;
    }
  }

  throw lastError instanceof Error ? lastError : new Error('No matching API endpoint responded');
}

export const api = {
  getDashboardSummary: () => request<DashboardSummary>('/api/v1/dashboard/summary'),
  getMarginGap: (params?: MarginGapParams) =>
    request<MarginGapResponse>(`/api/v1/margin-gap${buildQuery(params)}`),
  getMarginGapDrilldown: (ingredientId: string) =>
    request<MarginDrilldown>(`/api/v1/margin-gap/${ingredientId}/drilldown`),
  getInventoryLevels: () => request<InventoryLevel[]>('/api/v1/inventory/levels'),
  getReorderSuggestions: () => request<ReorderResponse>('/api/v1/inventory/reorder-suggestions'),
  getShrinkageReport: () => request<ShrinkageResponse>('/api/v1/shrinkage-report'),
  getBenchmarks: () => request<BenchmarksResponse>('/api/v1/benchmarks'),
  getVendorsScorecard: () => request<VendorResponse>('/api/v1/vendors/scorecard'),
  getPriceTrends: () => request<PriceTrendPoint[]>('/api/v1/price-trends'),
  getAlerts: () => request<AlertsResponse>('/api/v1/alerts'),
  getInvoiceQueue: async (): Promise<IngestionQueueResponse> => {
    const response = await requestFirstAvailable<IngestionQueueResponse | IngestionQueueItem[]>([
      '/api/v1/invoices/queue',
      '/api/v1/invoices/history',
      '/api/v1/invoices/status',
      '/api/v1/invoices/uploads',
    ]);

    return Array.isArray(response) ? { items: response } : response;
  },
  getInvoiceJobStatus: (jobId: string) =>
    requestFirstAvailable<InvoiceJobStatusResponse>([
      `/api/v1/invoices/jobs/${jobId}`,
      `/api/v1/invoices/status/${jobId}`,
      `/api/v1/invoices/${jobId}`,
    ]),
  uploadInvoice: async (file: File): Promise<InvoiceUploadResponse> => {
    const formData = new FormData();
    formData.append('file', file);
    const response = await fetch('/api/v1/invoices/upload', {
      method: 'POST',
      body: formData,
    });
    if (!response.ok) {
      throw new Error(`Invoice upload failed: ${response.status} ${response.statusText}`);
    }
    return response.json();
  },
};
