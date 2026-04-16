/**
 * Design reminder: industrial neo-noir command-center behavior; reliable, quiet, context-aware data loading.
 */
import { useEffect, useState } from 'react';

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
  const [usingFallback, setUsingFallback] = useState(false);

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
          setError(err instanceof Error ? err.message : 'Unable to reach API');
          setUsingFallback(true);
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
  }, [enabled, fallbackData, ...dependencies]);

  return { data, loading, error, usingFallback };
}
