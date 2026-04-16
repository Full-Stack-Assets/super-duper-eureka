from pathlib import Path
from textwrap import dedent

root = Path('/home/ubuntu/hostgraph-frontend')
client = root / 'client' / 'src'

files = {
    client / 'data' / 'mockData.ts': dedent('''
        export type TrendDirection = "up" | "down" | "flat";

        export interface KPIItem {
          title: string;
          value: string;
          delta: string;
          trend: TrendDirection;
          detail: string;
        }

        export interface ActionItem {
          title: string;
          description: string;
          owner: string;
          due: string;
          severity: "high" | "medium" | "low";
        }

        export interface LeakIngredient {
          ingredient: string;
          location: string;
          leakage: number;
          variancePct: number;
          issue: string;
        }

        export interface MarginGapRow {
          ingredientId: string;
          ingredient: string;
          category: string;
          location: string;
          actualCost: number;
          theoreticalCost: number;
          gapPct: number;
          benchmarkPct: number;
          vendor: string;
          issue: string;
        }

        export interface MarginDrilldown {
          ingredientId: string;
          ingredient: string;
          story: string;
          invoiceDelta: string;
          yieldDelta: string;
          benchmarkDelta: string;
          events: Array<{
            label: string;
            value: number;
          }>;
        }

        export interface ReorderSuggestion {
          sku: string;
          ingredient: string;
          location: string;
          onHand: string;
          projectedExhaustion: string;
          suggestedOrder: string;
          vendorBestPrice: string;
          alternateVendor: string;
          risk: "critical" | "watch" | "stable";
        }

        export interface VendorScorecardRow {
          vendor: string;
          onTimePct: number;
          fillRatePct: number;
          priceDriftPct: number;
          invoiceAccuracyPct: number;
          note: string;
        }

        export interface PriceTrendPoint {
          month: string;
          mozzarella: number;
          chicken: number;
          avocados: number;
        }

        export interface ShrinkageRow {
          location: string;
          ingredient: string;
          expectedYield: number;
          actualYield: number;
          variancePct: number;
          lossValue: number;
        }

        export interface BenchmarkSlice {
          name: string;
          value: number;
        }

        export interface AlertItem {
          id: string;
          severity: "critical" | "warning" | "info";
          title: string;
          detail: string;
          timestamp: string;
          location: string;
        }

        export interface InventoryLevel {
          ingredient: string;
          location: string;
          parLevel: number;
          onHand: number;
        }

        export interface DashboardSummary {
          kpis: KPIItem[];
          leakingIngredients: LeakIngredient[];
          actions: ActionItem[];
          benchmarkMix: BenchmarkSlice[];
          marginBridge: Array<{
            label: string;
            value: number;
          }>;
          narrative: string;
        }

        export interface MarginGapResponse {
          filters: {
            location: string;
            dateFrom: string;
            dateTo: string;
            category: string;
          };
          rows: MarginGapRow[];
          benchmarkOverlay: BenchmarkSlice[];
        }

        export interface ReorderResponse {
          suggestions: ReorderSuggestion[];
          inventoryLevels: InventoryLevel[];
        }

        export interface VendorResponse {
          scorecard: VendorScorecardRow[];
          priceTrends: PriceTrendPoint[];
          driftAlerts: AlertItem[];
        }

        export interface ShrinkageResponse {
          summary: KPIItem[];
          rows: ShrinkageRow[];
        }

        export interface AlertsResponse {
          alerts: AlertItem[];
        }

        export interface BenchmarksResponse {
          benchmarks: BenchmarkSlice[];
        }

        export const dashboardSummary: DashboardSummary = {
          kpis: [
            {
              title: 'Weekly margin leakage',
              value: '$18.4K',
              delta: '+3.2 pts vs last week',
              trend: 'up',
              detail: 'Driven by mozzarella, chicken trim, and late-night shrinkage.',
            },
            {
              title: 'Invoice overbilling flagged',
              value: '$6.2K',
              delta: '11 invoices need review',
              trend: 'up',
              detail: 'Sysco line items show repeated unit-cost drift above contract.',
            },
            {
              title: 'Yield variance exposure',
              value: '4.8%',
              delta: '+1.1 pts',
              trend: 'up',
              detail: 'South End and Cambridge are under-performing chicken prep yield.',
            },
            {
              title: 'Potential savings this cycle',
              value: '$12.7K',
              delta: 'If action items are completed',
              trend: 'down',
              detail: 'Recoverable through vendor negotiation and reorder discipline.',
            },
          ],
          leakingIngredients: [
            {
              ingredient: 'Whole milk mozzarella',
              location: 'Back Bay',
              leakage: 4200,
              variancePct: 14.8,
              issue: 'Vendor gouging above benchmark after contract reset.',
            },
            {
              ingredient: 'Chicken breast',
              location: 'South End',
              leakage: 3100,
              variancePct: 9.4,
              issue: 'Trim loss exceeded theoretical yield by 6.1 points.',
            },
            {
              ingredient: 'Avocados',
              location: 'Seaport',
              leakage: 1850,
              variancePct: 12.2,
              issue: 'Ripeness shrink and short-dated replacement credits missing.',
            },
            {
              ingredient: 'Fryer oil',
              location: 'Cambridge',
              leakage: 1360,
              variancePct: 8.1,
              issue: 'Usage cadence higher than production mix implies.',
            },
          ],
          actions: [
            {
              title: 'Challenge Sysco mozzarella invoices',
              description: 'Three Boston locations were billed 18–23% above contracted case cost this month.',
              owner: 'Finance Ops',
              due: 'Today 3:00 PM',
              severity: 'high',
            },
            {
              title: 'Retrain chicken trim station at South End',
              description: 'Observed yield is 78.2% vs theoretical 83.5%, costing roughly $1.9K per week.',
              owner: 'Culinary Ops',
              due: 'Tomorrow',
              severity: 'high',
            },
            {
              title: 'Shift avocado buy to FreshPoint for weekend run',
              description: 'Projected $0.17/lb lower delivered cost with better fill rate for Seaport.',
              owner: 'Procurement',
              due: 'Friday',
              severity: 'medium',
            },
          ],
          benchmarkMix: [
            { name: 'At benchmark', value: 61 },
            { name: 'Within tolerance', value: 24 },
            { name: 'Outside tolerance', value: 15 },
          ],
          marginBridge: [
            { label: 'Contract drift', value: 6200 },
            { label: 'Yield loss', value: 4700 },
            { label: 'Waste & shrink', value: 3900 },
            { label: 'Stockouts / rush buys', value: 3600 },
          ],
          narrative:
            'HostGraph mock data is centered on a Boston restaurant group where mozzarella contract pricing drift, chicken yield variance, and preventable shrinkage create visible “gotcha” moments during demos.',
        };

        export const marginGapData: MarginGapResponse = {
          filters: {
            location: 'All Boston locations',
            dateFrom: '2026-03-01',
            dateTo: '2026-03-31',
            category: 'All categories',
          },
          rows: [
            {
              ingredientId: 'mozz-001',
              ingredient: 'Whole milk mozzarella',
              category: 'Dairy',
              location: 'Back Bay',
              actualCost: 3.92,
              theoreticalCost: 3.22,
              gapPct: 21.7,
              benchmarkPct: 8.4,
              vendor: 'Sysco',
              issue: 'Invoice line cost reset above contracted case equivalent.',
            },
            {
              ingredientId: 'chk-002',
              ingredient: 'Chicken breast',
              category: 'Protein',
              location: 'South End',
              actualCost: 2.68,
              theoreticalCost: 2.31,
              gapPct: 16.0,
              benchmarkPct: 7.1,
              vendor: 'US Foods',
              issue: 'Yield loss and excess trim drive the gap more than price.',
            },
            {
              ingredientId: 'avo-003',
              ingredient: 'Avocados',
              category: 'Produce',
              location: 'Seaport',
              actualCost: 2.14,
              theoreticalCost: 1.87,
              gapPct: 14.4,
              benchmarkPct: 9.2,
              vendor: 'FreshPoint',
              issue: 'Shrink from ripeness window and missing credit memos.',
            },
            {
              ingredientId: 'oil-004',
              ingredient: 'Fryer oil',
              category: 'Dry goods',
              location: 'Cambridge',
              actualCost: 1.44,
              theoreticalCost: 1.28,
              gapPct: 12.5,
              benchmarkPct: 4.8,
              vendor: 'Restaurant Depot',
              issue: 'Usage cadence implies replacement too early in the cycle.',
            },
            {
              ingredientId: 'beef-005',
              ingredient: 'Ground beef',
              category: 'Protein',
              location: 'Beacon Hill',
              actualCost: 4.31,
              theoreticalCost: 3.98,
              gapPct: 8.3,
              benchmarkPct: 6.9,
              vendor: 'Performance Food Group',
              issue: 'Late-night substitution buying pushed average cost upward.',
            },
          ],
          benchmarkOverlay: [
            { name: 'Actual gap', value: 14.6 },
            { name: 'Peer benchmark', value: 7.3 },
            { name: 'Target tolerance', value: 5.0 },
          ],
        };

        export const marginDrilldowns: Record<string, MarginDrilldown> = {
          'mozz-001': {
            ingredientId: 'mozz-001',
            ingredient: 'Whole milk mozzarella',
            story:
              'Back Bay was billed for mozzarella at an effective $86.24 per case even though the contracted case rate was $70.80. The price spike appeared immediately after a distributor catalog refresh, making this a strong demo moment for invoice policing.',
            invoiceDelta: '+$4,200 over 4 weeks',
            yieldDelta: '+0.8 pts',
            benchmarkDelta: '+13.3 pts vs peers',
            events: [
              { label: 'Contracted', value: 70.8 },
              { label: 'Billed', value: 86.24 },
              { label: 'Peer median', value: 73.1 },
              { label: 'Recovered target', value: 71.2 },
            ],
          },
          'chk-002': {
            ingredientId: 'chk-002',
            ingredient: 'Chicken breast',
            story:
              'South End prep yield slipped to 78.2% after staffing changes. Invoice cost held mostly stable, so HostGraph isolates operational loss instead of incorrectly blaming vendor pricing.',
            invoiceDelta: '+$680 over 4 weeks',
            yieldDelta: '-5.3 pts vs standard',
            benchmarkDelta: '+8.9 pts vs peers',
            events: [
              { label: 'Theoretical yield', value: 83.5 },
              { label: 'Observed yield', value: 78.2 },
              { label: 'Waste trim', value: 11.6 },
              { label: 'Recovered target', value: 82.1 },
            ],
          },
          'avo-003': {
            ingredientId: 'avo-003',
            ingredient: 'Avocados',
            story:
              'Seaport is seeing shrink from over-ripeness and inconsistent quality credits. The gap is smaller than mozzarella, but it highlights produce volatility and vendor accountability during demos.',
            invoiceDelta: '+$1,050 over 4 weeks',
            yieldDelta: '-2.1 pts',
            benchmarkDelta: '+5.2 pts vs peers',
            events: [
              { label: 'Expected usable yield', value: 84.3 },
              { label: 'Actual usable yield', value: 82.2 },
              { label: 'Credit recovery', value: 37.0 },
              { label: 'Target credit recovery', value: 82.0 },
            ],
          },
          'oil-004': {
            ingredientId: 'oil-004',
            ingredient: 'Fryer oil',
            story:
              'Cambridge replacement cadence is occurring nearly a day earlier than its production mix supports, indicating either over-filtration issues or inaccurate line checks.',
            invoiceDelta: '+$520 over 4 weeks',
            yieldDelta: '-1.7 pts',
            benchmarkDelta: '+7.7 pts vs peers',
            events: [
              { label: 'Target change cycle', value: 6.5 },
              { label: 'Observed cycle', value: 5.3 },
              { label: 'Benchmark cycle', value: 6.1 },
              { label: 'Recovered target', value: 6.2 },
            ],
          },
          'beef-005': {
            ingredientId: 'beef-005',
            ingredient: 'Ground beef',
            story:
              'Beacon Hill has modest vendor drift, but the larger issue is stockout-driven spot buying on weekends when the preferred vendor cut-off is missed.',
            invoiceDelta: '+$760 over 4 weeks',
            yieldDelta: '+0.2 pts',
            benchmarkDelta: '+1.4 pts vs peers',
            events: [
              { label: 'Preferred vendor', value: 3.98 },
              { label: 'Emergency buy', value: 4.46 },
              { label: 'Benchmark', value: 4.01 },
              { label: 'Recovered target', value: 3.99 },
            ],
          },
        };

        export const inventoryLevels: InventoryLevel[] = [
          { ingredient: 'Whole milk mozzarella', location: 'Back Bay', parLevel: 48, onHand: 19 },
          { ingredient: 'Chicken breast', location: 'South End', parLevel: 64, onHand: 21 },
          { ingredient: 'Avocados', location: 'Seaport', parLevel: 54, onHand: 18 },
          { ingredient: 'Burger buns', location: 'Beacon Hill', parLevel: 90, onHand: 41 },
        ];

        export const reorderData: ReorderResponse = {
          suggestions: [
            {
              sku: 'MOZ-6LB',
              ingredient: 'Whole milk mozzarella',
              location: 'Back Bay',
              onHand: '19 cases',
              projectedExhaustion: 'In 2.1 days',
              suggestedOrder: '34 cases',
              vendorBestPrice: '$71.20 / case',
              alternateVendor: 'Chefs Warehouse',
              risk: 'critical',
            },
            {
              sku: 'CHK-40LB',
              ingredient: 'Chicken breast',
              location: 'South End',
              onHand: '21 cases',
              projectedExhaustion: 'In 1.7 days',
              suggestedOrder: '42 cases',
              vendorBestPrice: '$91.40 / case',
              alternateVendor: 'US Foods',
              risk: 'critical',
            },
            {
              sku: 'AVO-HASS',
              ingredient: 'Avocados',
              location: 'Seaport',
              onHand: '18 trays',
              projectedExhaustion: 'In 2.8 days',
              suggestedOrder: '26 trays',
              vendorBestPrice: '$29.10 / tray',
              alternateVendor: 'FreshPoint',
              risk: 'watch',
            },
            {
              sku: 'BUN-BRIOCHE',
              ingredient: 'Burger buns',
              location: 'Beacon Hill',
              onHand: '41 racks',
              projectedExhaustion: 'In 4.6 days',
              suggestedOrder: '24 racks',
              vendorBestPrice: '$13.80 / rack',
              alternateVendor: 'Baldor',
              risk: 'stable',
            },
          ],
          inventoryLevels,
        };

        export const vendorData: VendorResponse = {
          scorecard: [
            {
              vendor: 'Sysco',
              onTimePct: 92,
              fillRatePct: 95,
              priceDriftPct: 12.4,
              invoiceAccuracyPct: 81,
              note: 'Primary concern: mozzarella pricing above contract and delayed credits.',
            },
            {
              vendor: 'US Foods',
              onTimePct: 97,
              fillRatePct: 96,
              priceDriftPct: 4.1,
              invoiceAccuracyPct: 94,
              note: 'Stable pricing, but South End chicken yield issue is operational rather than vendor-led.',
            },
            {
              vendor: 'FreshPoint',
              onTimePct: 95,
              fillRatePct: 93,
              priceDriftPct: 6.8,
              invoiceAccuracyPct: 91,
              note: 'Produce quality is mixed; avocado credits inconsistent at Seaport.',
            },
            {
              vendor: 'Restaurant Depot',
              onTimePct: 88,
              fillRatePct: 90,
              priceDriftPct: 2.4,
              invoiceAccuracyPct: 96,
              note: 'Good spot-buy partner, but operational discipline matters more than price.',
            },
          ],
          priceTrends: [
            { month: 'Nov', mozzarella: 71, chicken: 89, avocados: 26 },
            { month: 'Dec', mozzarella: 72, chicken: 90, avocados: 28 },
            { month: 'Jan', mozzarella: 73, chicken: 92, avocados: 27 },
            { month: 'Feb', mozzarella: 74, chicken: 91, avocados: 31 },
            { month: 'Mar', mozzarella: 86, chicken: 91, avocados: 29 },
            { month: 'Apr', mozzarella: 85, chicken: 93, avocados: 30 },
          ],
          driftAlerts: [
            {
              id: 'alert-sysco-mozz',
              severity: 'critical',
              title: 'Mozzarella price gouging detected',
              detail: 'Sysco billed Back Bay 21.7% above theoretical cost and 13.3 pts above peer benchmark.',
              timestamp: '12 minutes ago',
              location: 'Back Bay',
            },
            {
              id: 'alert-freshpoint-avo',
              severity: 'warning',
              title: 'Avocado credits lagging behind shrink trend',
              detail: 'Seaport shrink claims outpaced posted vendor credits for 3 straight deliveries.',
              timestamp: '1 hour ago',
              location: 'Seaport',
            },
          ],
        };

        export const shrinkageData: ShrinkageResponse = {
          summary: [
            {
              title: 'Weekly shrink exposure',
              value: '$5.6K',
              delta: '+9% vs prior week',
              trend: 'up',
              detail: 'Night prep and produce spoilage remain the main loss drivers.',
            },
            {
              title: 'Average yield gap',
              value: '3.4 pts',
              delta: '+0.6 pts',
              trend: 'up',
              detail: 'Chicken and avocado handling are widening the gap.',
            },
          ],
          rows: [
            {
              location: 'South End',
              ingredient: 'Chicken breast',
              expectedYield: 83.5,
              actualYield: 78.2,
              variancePct: -5.3,
              lossValue: 1910,
            },
            {
              location: 'Seaport',
              ingredient: 'Avocados',
              expectedYield: 84.3,
              actualYield: 82.2,
              variancePct: -2.1,
              lossValue: 980,
            },
            {
              location: 'Cambridge',
              ingredient: 'Fryer oil',
              expectedYield: 100,
              actualYield: 96.4,
              variancePct: -3.6,
              lossValue: 720,
            },
            {
              location: 'Back Bay',
              ingredient: 'Romaine',
              expectedYield: 92.4,
              actualYield: 89.8,
              variancePct: -2.6,
              lossValue: 640,
            },
          ],
        };

        export const alertsData: AlertsResponse = {
          alerts: [
            {
              id: 'a-1',
              severity: 'critical',
              title: 'Sysco overbilling flagged on mozzarella invoices',
              detail: 'Three locations crossed contract tolerance, generating an estimated $6.2K monthly overcharge.',
              timestamp: '8 minutes ago',
              location: 'Back Bay / Cambridge / Beacon Hill',
            },
            {
              id: 'a-2',
              severity: 'critical',
              title: 'South End chicken yield slipped below threshold',
              detail: 'Observed usable yield fell to 78.2%, increasing effective cost per plate immediately.',
              timestamp: '34 minutes ago',
              location: 'South End',
            },
            {
              id: 'a-3',
              severity: 'warning',
              title: 'Avocado shrink not matched by vendor credit',
              detail: 'FreshPoint credits cover only 45% of reported produce loss over the last 2 weeks.',
              timestamp: '1 hour ago',
              location: 'Seaport',
            },
            {
              id: 'a-4',
              severity: 'info',
              title: 'Beacon Hill reorder suggestion could avoid emergency beef buy',
              detail: 'Recommended reorder timing is expected to reduce weekend spot buys by 18%.',
              timestamp: 'Today',
              location: 'Beacon Hill',
            },
          ],
        };

        export const benchmarksData: BenchmarksResponse = {
          benchmarks: [
            { name: 'Boston portfolio', value: 14.6 },
            { name: 'Peer top quartile', value: 6.3 },
            { name: 'Peer median', value: 7.3 },
          ],
        };

        export const mockDataRegistry = {
          dashboardSummary,
          marginGap: marginGapData,
          marginGapDrilldown: marginDrilldowns,
          inventoryLevels,
          reorderSuggestions: reorderData,
          shrinkageReport: shrinkageData,
          benchmarks: benchmarksData,
          vendorsScorecard: vendorData,
          priceTrends: vendorData.priceTrends,
          alerts: alertsData,
        };
    '''),
    client / 'services' / 'api.ts': dedent('''
        import type {
          AlertsResponse,
          BenchmarksResponse,
          DashboardSummary,
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

        const buildQuery = (params?: Record<string, string | undefined>) => {
          const search = new URLSearchParams();
          Object.entries(params ?? {}).forEach(([key, value]) => {
            if (value) search.set(key, value);
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
          uploadInvoice: async (file: File) => {
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
    '''),
    client / 'hooks' / 'useFetch.ts': dedent('''
        import { useEffect, useMemo, useState } from 'react';

        interface UseFetchOptions<T> {
          fallbackData: T;
          dependencies?: readonly unknown[];
          enabled?: boolean;
        }

        export function useFetch<T>(
          fetcher: () => Promise<T>,
          { fallbackData, dependencies = [], enabled = true }: UseFetchOptions<T>,
        ) {
          const [data, setData] = useState<T>(fallbackData);
          const [loading, setLoading] = useState<boolean>(enabled);
          const [error, setError] = useState<string | null>(null);
          const [usingFallback, setUsingFallback] = useState<boolean>(false);

          const stableDependencies = useMemo(() => dependencies, dependencies);

          useEffect(() => {
            if (!enabled) {
              setLoading(false);
              return;
            }

            let cancelled = false;

            const run = async () => {
              setLoading(true);
              setError(null);
              try {
                const result = await fetcher();
                if (!cancelled) {
                  setData(result);
                  setUsingFallback(false);
                }
              } catch (err) {
                if (!cancelled) {
                  setData(fallbackData);
                  setUsingFallback(true);
                  setError(err instanceof Error ? err.message : 'Unknown API error');
                }
              } finally {
                if (!cancelled) {
                  setLoading(false);
                }
              }
            };

            run();

            return () => {
              cancelled = true;
            };
          }, [enabled, fallbackData, fetcher, ...stableDependencies]);

          return { data, loading, error, usingFallback };
        }
    '''),
}

for path, content in files.items():
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + '\n', encoding='utf-8')
