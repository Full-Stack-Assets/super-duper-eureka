from pathlib import Path
from textwrap import dedent

root = Path('/home/ubuntu/hostgraph-frontend')
client = root / 'client' / 'src'
hero = 'https://d2xsxph8kpxj0f.cloudfront.net/310519663540603382/KRgpskTa3UjstPtv6w78ES/hostgraph-hero-command-center-jgcqa6jkAuyiHbfhJMadhU.webp'
margin = 'https://d2xsxph8kpxj0f.cloudfront.net/310519663540603382/KRgpskTa3UjstPtv6w78ES/hostgraph-margin-gap-surface-7f8RdeFJ8zuyyHTLKeXSkH.webp'
vendor = 'https://d2xsxph8kpxj0f.cloudfront.net/310519663540603382/KRgpskTa3UjstPtv6w78ES/hostgraph-vendor-network-4gKUJ8bWcc6RN7G3PScBaC.webp'
alerts = 'https://d2xsxph8kpxj0f.cloudfront.net/310519663540603382/KRgpskTa3UjstPtv6w78ES/hostgraph-alerts-pulse-ATNXMeoLi5seV6giqm5WfA.webp'

files = {
    client / 'hooks' / 'useFetch.ts': dedent('''
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
    '''),
    client / 'components' / 'HostGraphShell.tsx': dedent('''
        /**
         * Design reminder: industrial neo-noir command rail with asymmetrical layout, luminous dividers, and disciplined typography.
         */
        import { cn } from '@/lib/utils';
        import {
          AlertTriangle,
          ArrowRightLeft,
          BellRing,
          ChartColumnIncreasing,
          ChevronRight,
          CircleDollarSign,
          PackageSearch,
          Store,
          Wheat,
        } from 'lucide-react';
        import { NavLink, Outlet } from 'react-router-dom';

        const navItems = [
          { label: 'Dashboard Summary', to: '/', icon: ChartColumnIncreasing },
          { label: 'Margin Gap Report', to: '/margin-gap', icon: CircleDollarSign },
          { label: 'Reorder Suggestions', to: '/reorder', icon: PackageSearch },
          { label: 'Vendor Scorecard', to: '/vendors', icon: Store },
          { label: 'Shrinkage & Yield', to: '/shrinkage', icon: Wheat },
          { label: 'Alerts', to: '/alerts', icon: BellRing },
        ];

        export function HostGraphShell() {
          return (
            <div className="min-h-screen bg-background text-foreground">
              <div className="pointer-events-none fixed inset-0 bg-[radial-gradient(circle_at_top_left,rgba(16,185,129,0.10),transparent_24%),radial-gradient(circle_at_bottom_right,rgba(239,68,68,0.08),transparent_18%)]" />
              <div className="pointer-events-none fixed inset-0 opacity-[0.04] mix-blend-screen [background-image:linear-gradient(rgba(255,255,255,0.08)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.08)_1px,transparent_1px)] [background-size:32px_32px]" />
              <div className="relative grid min-h-screen lg:grid-cols-[280px_minmax(0,1fr)]">
                <aside className="border-r border-white/8 bg-sidebar/80 px-5 py-6 backdrop-blur-xl">
                  <div className="flex h-full flex-col gap-6">
                    <div className="space-y-4">
                      <div className="inline-flex items-center gap-2 rounded-full border border-emerald-400/20 bg-emerald-400/10 px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.28em] text-emerald-200">
                        <ArrowRightLeft className="size-3" />
                        Procurement command center
                      </div>
                      <div>
                        <p className="font-mono text-xs uppercase tracking-[0.32em] text-zinc-500">HostGraph</p>
                        <h1 className="mt-2 text-3xl font-semibold tracking-tight text-white">Boston portfolio control tower</h1>
                        <p className="mt-3 max-w-xs text-sm leading-6 text-zinc-400">
                          A live procurement cockpit focused on margin leakage, vendor drift, and store-level yield discipline.
                        </p>
                      </div>
                    </div>

                    <nav className="space-y-2">
                      {navItems.map(({ label, to, icon: Icon }) => (
                        <NavLink
                          key={to}
                          to={to}
                          end={to === '/'}
                          className={({ isActive }) =>
                            cn(
                              'group flex items-center justify-between rounded-2xl border px-4 py-3 transition-all duration-200',
                              isActive
                                ? 'border-emerald-400/30 bg-emerald-400/12 text-white shadow-[0_0_0_1px_rgba(16,185,129,0.1)]'
                                : 'border-white/5 bg-white/[0.02] text-zinc-400 hover:border-white/10 hover:bg-white/[0.04] hover:text-zinc-100',
                            )
                          }
                        >
                          {({ isActive }) => (
                            <>
                              <span className="flex items-center gap-3 text-sm font-medium">
                                <span
                                  className={cn(
                                    'flex size-9 items-center justify-center rounded-xl border transition-colors',
                                    isActive
                                      ? 'border-emerald-400/30 bg-emerald-400/10 text-emerald-200'
                                      : 'border-white/8 bg-black/20 text-zinc-500 group-hover:text-zinc-200',
                                  )}
                                >
                                  <Icon className="size-4" />
                                </span>
                                {label}
                              </span>
                              <ChevronRight className={cn('size-4 transition-transform', isActive ? 'text-emerald-200' : 'text-zinc-600 group-hover:translate-x-0.5')} />
                            </>
                          )}
                        </NavLink>
                      ))}
                    </nav>

                    <div className="mt-auto rounded-[28px] border border-white/8 bg-black/20 p-4 shadow-[inset_0_1px_0_rgba(255,255,255,0.04)]">
                      <p className="font-mono text-[11px] uppercase tracking-[0.32em] text-zinc-500">Demo narrative</p>
                      <h2 className="mt-3 text-lg font-semibold text-white">The gotcha trilogy</h2>
                      <ul className="mt-4 space-y-3 text-sm text-zinc-400">
                        <li>Sysco overbilling on mozzarella contracts</li>
                        <li>Chicken yield variance after staffing change</li>
                        <li>Avocado shrink without matching credits</li>
                      </ul>
                    </div>
                  </div>
                </aside>

                <main className="relative min-w-0 px-4 py-4 sm:px-6 sm:py-6 lg:px-8">
                  <Outlet />
                </main>
              </div>
            </div>
          );
        }
    '''),
    client / 'components' / 'dashboard-primitives.tsx': dedent('''
        /**
         * Design reminder: machined information surfaces, mono numerics, subtle glow accents, and strong contrast on dark glass panels.
         */
        import { cn } from '@/lib/utils';
        import { Badge } from '@/components/ui/badge';
        import type { ReactNode } from 'react';
        import { AlertTriangle, Info, LoaderCircle, TriangleAlert, TrendingDown, TrendingUp } from 'lucide-react';

        export function formatCurrency(value: number) {
          return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            maximumFractionDigits: 0,
          }).format(value);
        }

        export function formatCurrencyCompact(value: number) {
          return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            notation: 'compact',
            maximumFractionDigits: 1,
          }).format(value);
        }

        export function formatPercent(value: number) {
          return `${value.toFixed(1)}%`;
        }

        export function Surface({ children, className }: { children: ReactNode; className?: string }) {
          return (
            <section
              className={cn(
                'rounded-[28px] border border-white/8 bg-card/80 p-5 shadow-[0_20px_80px_rgba(0,0,0,0.28),inset_0_1px_0_rgba(255,255,255,0.03)] backdrop-blur-xl',
                className,
              )}
            >
              {children}
            </section>
          );
        }

        export function HeroPanel({
          eyebrow,
          title,
          description,
          image,
          children,
          className,
        }: {
          eyebrow: string;
          title: string;
          description: string;
          image: string;
          children?: ReactNode;
          className?: string;
        }) {
          return (
            <section
              className={cn(
                'overflow-hidden rounded-[34px] border border-white/8 bg-zinc-950 shadow-[0_24px_100px_rgba(0,0,0,0.45)]',
                className,
              )}
            >
              <div className="grid gap-0 lg:grid-cols-[minmax(0,1.25fr)_minmax(280px,0.75fr)]">
                <div className="relative min-h-[320px] overflow-hidden p-6 sm:p-8 lg:p-10">
                  <div
                    className="absolute inset-0 bg-cover bg-center"
                    style={{ backgroundImage: `linear-gradient(90deg, rgba(4,7,11,0.94) 0%, rgba(4,7,11,0.82) 46%, rgba(4,7,11,0.46) 100%), url(${image})` }}
                  />
                  <div className="absolute inset-0 bg-[linear-gradient(to_bottom,rgba(16,185,129,0.08),transparent_40%,rgba(239,68,68,0.08))]" />
                  <div className="relative flex h-full flex-col justify-between gap-8">
                    <div className="space-y-4">
                      <p className="font-mono text-[11px] uppercase tracking-[0.34em] text-emerald-200/80">{eyebrow}</p>
                      <div className="max-w-2xl space-y-4">
                        <h2 className="max-w-xl text-4xl font-semibold tracking-tight text-white sm:text-5xl">{title}</h2>
                        <p className="max-w-2xl text-sm leading-7 text-zinc-300 sm:text-base">{description}</p>
                      </div>
                    </div>
                    {children}
                  </div>
                </div>
                <div className="border-t border-white/8 bg-black/25 p-6 lg:border-l lg:border-t-0">{children}</div>
              </div>
            </section>
          );
        }

        export function MetricCard({
          title,
          value,
          delta,
          detail,
          trend,
        }: {
          title: string;
          value: string;
          delta: string;
          detail: string;
          trend: 'up' | 'down' | 'flat';
        }) {
          const icon = trend === 'up' ? TrendingUp : trend === 'down' ? TrendingDown : Info;
          const Icon = icon;
          const tone = trend === 'up' ? 'text-red-300' : trend === 'down' ? 'text-emerald-300' : 'text-zinc-300';

          return (
            <Surface className="group h-full transition-transform duration-200 hover:-translate-y-0.5">
              <div className="flex items-start justify-between gap-4">
                <div>
                  <p className="text-sm text-zinc-400">{title}</p>
                  <div className="mt-4 flex items-end gap-3">
                    <p className="font-mono text-3xl font-semibold tracking-tight text-white">{value}</p>
                    <span className={cn('mb-1 inline-flex items-center gap-1 text-xs font-medium', tone)}>
                      <Icon className="size-3.5" />
                      {delta}
                    </span>
                  </div>
                </div>
                <span className="rounded-full border border-white/10 bg-white/5 px-2 py-1 font-mono text-[11px] uppercase tracking-[0.24em] text-zinc-500">
                  Live
                </span>
              </div>
              <p className="mt-5 text-sm leading-6 text-zinc-400">{detail}</p>
            </Surface>
          );
        }

        export function SectionHeading({
          eyebrow,
          title,
          description,
          aside,
        }: {
          eyebrow: string;
          title: string;
          description: string;
          aside?: ReactNode;
        }) {
          return (
            <div className="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
              <div className="space-y-3">
                <p className="font-mono text-[11px] uppercase tracking-[0.34em] text-zinc-500">{eyebrow}</p>
                <div>
                  <h3 className="text-2xl font-semibold tracking-tight text-white">{title}</h3>
                  <p className="mt-2 max-w-3xl text-sm leading-6 text-zinc-400">{description}</p>
                </div>
              </div>
              {aside}
            </div>
          );
        }

        export function PageStateBanner({ usingFallback, error }: { usingFallback?: boolean; error?: string | null }) {
          if (!usingFallback && !error) return null;
          return (
            <div className="flex items-start gap-3 rounded-2xl border border-amber-400/20 bg-amber-400/10 px-4 py-3 text-sm text-amber-100">
              <TriangleAlert className="mt-0.5 size-4 shrink-0" />
              <div>
                <p className="font-medium">Showing standalone demo data</p>
                <p className="mt-1 text-amber-100/80">
                  The live API was unavailable, so HostGraph fell back to the mock Boston restaurant-group storyline.
                  {error ? ` Last error: ${error}` : ''}
                </p>
              </div>
            </div>
          );
        }

        export function LoadingPanel({ label = 'Loading procurement intelligence…' }: { label?: string }) {
          return (
            <Surface className="flex min-h-[220px] items-center justify-center">
              <div className="flex items-center gap-3 text-zinc-300">
                <LoaderCircle className="size-5 animate-spin text-emerald-300" />
                <span className="text-sm">{label}</span>
              </div>
            </Surface>
          );
        }

        export function SeverityBadge({ severity }: { severity: 'critical' | 'warning' | 'info' | 'high' | 'medium' | 'low' | 'critical' | 'watch' | 'stable' }) {
          const styles: Record<string, string> = {
            critical: 'border-red-400/20 bg-red-400/10 text-red-200',
            warning: 'border-amber-400/20 bg-amber-400/10 text-amber-200',
            info: 'border-cyan-400/20 bg-cyan-400/10 text-cyan-200',
            high: 'border-red-400/20 bg-red-400/10 text-red-200',
            medium: 'border-amber-400/20 bg-amber-400/10 text-amber-200',
            low: 'border-emerald-400/20 bg-emerald-400/10 text-emerald-200',
            watch: 'border-amber-400/20 bg-amber-400/10 text-amber-200',
            stable: 'border-emerald-400/20 bg-emerald-400/10 text-emerald-200',
          };
          return <Badge className={cn('rounded-full border px-2.5 py-1 text-[11px] uppercase tracking-[0.24em]', styles[severity])}>{severity}</Badge>;
        }

        export function EmptyCopy({ title, detail }: { title: string; detail: string }) {
          return (
            <Surface className="flex min-h-[220px] items-center justify-center text-center">
              <div className="max-w-md space-y-3">
                <AlertTriangle className="mx-auto size-8 text-zinc-500" />
                <h4 className="text-lg font-semibold text-white">{title}</h4>
                <p className="text-sm leading-6 text-zinc-400">{detail}</p>
              </div>
            </Surface>
          );
        }
    '''),
    client / 'pages' / 'DashboardPage.tsx': dedent('''
        /**
         * Design reminder: industrial neo-noir command-center dashboard with staggered analysis bands and restrained alert accents.
         */
        import {{ DonutChart, BarChart }} from '@tremor/react';
        import {{ useCallback }} from 'react';
        import {{ api }} from '@/services/api';
        import {{ dashboardSummary }} from '@/data/mockData';
        import {{ useFetch }} from '@/hooks/useFetch';
        import {{
          formatCurrencyCompact,
          HeroPanel,
          LoadingPanel,
          MetricCard,
          PageStateBanner,
          SectionHeading,
          SeverityBadge,
          Surface,
        }} from '@/components/dashboard-primitives';

        export default function DashboardPage() {{
          const fetchDashboard = useCallback(() => api.getDashboardSummary(), []);
          const {{ data, loading, error, usingFallback }} = useFetch(fetchDashboard, {{ fallbackData: dashboardSummary }});

          if (loading) return <LoadingPanel label="Booting dashboard summary…" />;

          return (
            <div className="space-y-6">
              <HeroPanel
                eyebrow="Portfolio overview"
                title="Margin leakage mapped across the Boston fleet"
                description="HostGraph surfaces where margin slips away first: contract drift, yield loss, missing credits, and reorder timing. The dashboard is designed as a control surface rather than a passive report."
                image="https://d2xsxph8kpxj0f.cloudfront.net/310519663540603382/KRgpskTa3UjstPtv6w78ES/hostgraph-hero-command-center-jgcqa6jkAuyiHbfhJMadhU.webp"
              >
                <div className="grid gap-4 xl:grid-cols-2">
                  <Surface className="bg-black/20">
                    <p className="font-mono text-[11px] uppercase tracking-[0.32em] text-zinc-500">Command note</p>
                    <p className="mt-3 text-sm leading-7 text-zinc-300">{{data.narrative}}</p>
                  </Surface>
                  <Surface className="bg-black/20">
                    <p className="font-mono text-[11px] uppercase tracking-[0.32em] text-zinc-500">Immediate focus</p>
                    <div className="mt-3 space-y-3 text-sm text-zinc-300">
                      <div className="flex items-center justify-between"><span>Sysco invoice drift</span><span className="font-mono text-red-300">$6.2K</span></div>
                      <div className="flex items-center justify-between"><span>Chicken yield loss</span><span className="font-mono text-amber-200">5.3 pts</span></div>
                      <div className="flex items-center justify-between"><span>Recoverable this cycle</span><span className="font-mono text-emerald-300">$12.7K</span></div>
                    </div>
                  </Surface>
                </div>
              </HeroPanel>

              <PageStateBanner usingFallback={{usingFallback}} error={{error}} />

              <section className="grid gap-4 xl:grid-cols-4">
                {{data.kpis.map((item) => (
                  <MetricCard key={{item.title}} {{...item}} />
                ))}}
              </section>

              <section className="grid gap-6 xl:grid-cols-[1.2fr_0.8fr]">
                <Surface>
                  <SectionHeading
                    eyebrow="Leak map"
                    title="Top leaking ingredients"
                    description="The highest-value margin leaks combine price drift and operational waste. In the demo story, mozzarella creates the strongest reaction because the contract miss is immediately obvious."
                  />
                  <div className="mt-6 h-80">
                    <BarChart
                      className="h-80"
                      data={{data.leakingIngredients}}
                      index="ingredient"
                      categories={{['leakage']}}
                      colors={{['emerald']}}
                      showLegend={{false}}
                      valueFormatter={{formatCurrencyCompact}}
                      yAxisWidth={{64}}
                    />
                  </div>
                </Surface>

                <Surface>
                  <SectionHeading
                    eyebrow="Benchmark mix"
                    title="Portfolio tolerance split"
                    description="A quick view of how much spend sits at benchmark, near tolerance, or fully outside range."
                  />
                  <div className="mt-6 flex flex-col gap-6 lg:flex-row lg:items-center">
                    <DonutChart
                      className="mx-auto h-52"
                      data={{data.benchmarkMix}}
                      category="value"
                      index="name"
                      colors={{['emerald', 'cyan', 'rose']}}
                      valueFormatter={{(value) => `${{value}}%`}}
                    />
                    <div className="space-y-4">
                      {{data.benchmarkMix.map((slice) => (
                        <div key={{slice.name}} className="rounded-2xl border border-white/8 bg-white/[0.03] px-4 py-3">
                          <div className="flex items-center justify-between gap-4">
                            <p className="text-sm text-zinc-300">{{slice.name}}</p>
                            <span className="font-mono text-base text-white">{{slice.value}}%</span>
                          </div>
                        </div>
                      ))}}
                    </div>
                  </div>
                </Surface>
              </section>

              <section className="grid gap-6 xl:grid-cols-[0.95fr_1.05fr]">
                <Surface>
                  <SectionHeading
                    eyebrow="Action board"
                    title="Priority action items"
                    description="These are the highest-confidence interventions the operations team can take this week."
                  />
                  <div className="mt-6 space-y-4">
                    {{data.actions.map((action) => (
                      <div key={{action.title}} className="rounded-3xl border border-white/8 bg-white/[0.03] p-4">
                        <div className="flex flex-wrap items-center justify-between gap-3">
                          <h4 className="text-base font-medium text-white">{{action.title}}</h4>
                          <SeverityBadge severity={{action.severity}} />
                        </div>
                        <p className="mt-3 text-sm leading-6 text-zinc-400">{{action.description}}</p>
                        <div className="mt-4 flex flex-wrap items-center gap-4 font-mono text-[11px] uppercase tracking-[0.24em] text-zinc-500">
                          <span>Owner {{action.owner}}</span>
                          <span>Due {{action.due}}</span>
                        </div>
                      </div>
                    ))}}
                  </div>
                </Surface>

                <Surface>
                  <SectionHeading
                    eyebrow="Bridge"
                    title="What is driving the margin gap"
                    description="A compact driver bridge that helps the operator separate procurement, waste, and service-level causes."
                  />
                  <div className="mt-6 grid gap-4 sm:grid-cols-2">
                    {{data.marginBridge.map((driver) => (
                      <div key={{driver.label}} className="rounded-3xl border border-white/8 bg-gradient-to-br from-white/[0.05] to-white/[0.02] p-5">
                        <p className="text-sm text-zinc-400">{{driver.label}}</p>
                        <p className="mt-3 font-mono text-3xl text-white">{{formatCurrencyCompact(driver.value)}}</p>
                      </div>
                    ))}}
                  </div>
                </Surface>
              </section>
            </div>
          );
        }}
    '''),
    client / 'pages' / 'MarginGapPage.tsx': dedent('''
        /**
         * Design reminder: this is the hero analytical view; prioritize full-width tables, benchmark overlays, and contextual drill-down instead of symmetric card grids.
         */
        import {{ BarChart, DonutChart }} from '@tremor/react';
        import {{ useCallback, useMemo, useState }} from 'react';
        import {{ api }} from '@/services/api';
        import {{ marginDrilldowns, marginGapData }} from '@/data/mockData';
        import {{ useFetch }} from '@/hooks/useFetch';
        import {{
          formatPercent,
          HeroPanel,
          LoadingPanel,
          PageStateBanner,
          SectionHeading,
          Surface,
        }} from '@/components/dashboard-primitives';

        const defaultFilters = {{
          location: 'All Boston locations',
          dateFrom: '2026-03-01',
          dateTo: '2026-03-31',
          category: 'All categories',
        }};

        export default function MarginGapPage() {{
          const [filters, setFilters] = useState(defaultFilters);
          const [selectedIngredientId, setSelectedIngredientId] = useState(marginGapData.rows[0]?.ingredientId ?? '');

          const fetchMarginGap = useCallback(
            () =>
              api.getMarginGap({{
                location: filters.location,
                dateFrom: filters.dateFrom,
                dateTo: filters.dateTo,
                category: filters.category,
              }}),
            [filters.category, filters.dateFrom, filters.dateTo, filters.location],
          );

          const marginResponse = useFetch(fetchMarginGap, {{
            fallbackData: marginGapData,
            dependencies: [filters.location, filters.dateFrom, filters.dateTo, filters.category],
          }});

          const activeId = selectedIngredientId || marginResponse.data.rows[0]?.ingredientId || '';

          const fetchDrilldown = useCallback(() => api.getMarginGapDrilldown(activeId), [activeId]);
          const drilldownResponse = useFetch(fetchDrilldown, {{
            fallbackData: marginDrilldowns[activeId] ?? marginDrilldowns['mozz-001'],
            dependencies: [activeId],
            enabled: Boolean(activeId),
          }});

          const overlayData = useMemo(
            () =>
              marginResponse.data.benchmarkOverlay.map((slice) => ({
                ...slice,
                value: Number(slice.value.toFixed(1)),
              })),
            [marginResponse.data.benchmarkOverlay],
          );

          if (marginResponse.loading) return <LoadingPanel label="Loading margin-gap hero view…" />;

          return (
            <div className="space-y-6">
              <HeroPanel
                eyebrow="Hero view"
                title="Where actual cost breaks away from theory"
                description="The Margin Gap report turns procurement leakage into an operator workflow. Filter by location, date range, and category, then move directly into ingredient-level drill-down to isolate price drift, yield loss, and benchmark variance."
                image="https://d2xsxph8kpxj0f.cloudfront.net/310519663540603382/KRgpskTa3UjstPtv6w78ES/hostgraph-margin-gap-surface-7f8RdeFJ8zuyyHTLKeXSkH.webp"
              >
                <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-4">
                  <label className="space-y-2 text-sm text-zinc-300">
                    <span className="block font-mono text-[11px] uppercase tracking-[0.28em] text-zinc-500">Location</span>
                    <select
                      value={{filters.location}}
                      onChange={{(event) => setFilters((current) => ({{ ...current, location: event.target.value }}))}}
                      className="w-full rounded-2xl border border-white/10 bg-black/30 px-4 py-3 text-sm text-white outline-none transition focus:border-emerald-400/40"
                    >
                      <option>All Boston locations</option>
                      <option>Back Bay</option>
                      <option>South End</option>
                      <option>Seaport</option>
                      <option>Cambridge</option>
                      <option>Beacon Hill</option>
                    </select>
                  </label>
                  <label className="space-y-2 text-sm text-zinc-300">
                    <span className="block font-mono text-[11px] uppercase tracking-[0.28em] text-zinc-500">Date from</span>
                    <input
                      type="date"
                      value={{filters.dateFrom}}
                      onChange={{(event) => setFilters((current) => ({{ ...current, dateFrom: event.target.value }}))}}
                      className="w-full rounded-2xl border border-white/10 bg-black/30 px-4 py-3 text-sm text-white outline-none transition focus:border-emerald-400/40"
                    />
                  </label>
                  <label className="space-y-2 text-sm text-zinc-300">
                    <span className="block font-mono text-[11px] uppercase tracking-[0.28em] text-zinc-500">Date to</span>
                    <input
                      type="date"
                      value={{filters.dateTo}}
                      onChange={{(event) => setFilters((current) => ({{ ...current, dateTo: event.target.value }}))}}
                      className="w-full rounded-2xl border border-white/10 bg-black/30 px-4 py-3 text-sm text-white outline-none transition focus:border-emerald-400/40"
                    />
                  </label>
                  <label className="space-y-2 text-sm text-zinc-300">
                    <span className="block font-mono text-[11px] uppercase tracking-[0.28em] text-zinc-500">Category</span>
                    <select
                      value={{filters.category}}
                      onChange={{(event) => setFilters((current) => ({{ ...current, category: event.target.value }}))}}
                      className="w-full rounded-2xl border border-white/10 bg-black/30 px-4 py-3 text-sm text-white outline-none transition focus:border-emerald-400/40"
                    >
                      <option>All categories</option>
                      <option>Dairy</option>
                      <option>Protein</option>
                      <option>Produce</option>
                      <option>Dry goods</option>
                    </select>
                  </label>
                </div>
              </HeroPanel>

              <PageStateBanner usingFallback={{marginResponse.usingFallback || drilldownResponse.usingFallback}} error={{marginResponse.error || drilldownResponse.error}} />

              <section className="grid gap-6 xl:grid-cols-[1.18fr_0.82fr]">
                <Surface>
                  <SectionHeading
                    eyebrow="Variance ledger"
                    title="Actual versus theoretical cost by ingredient"
                    description="Click any row to load the right-hand drill-down. The most convincing story in the demo is the mozzarella contract breach because the benchmark overlay stays calm while actual cost spikes."
                  />
                  <div className="mt-6 overflow-hidden rounded-[28px] border border-white/8">
                    <div className="overflow-x-auto">
                      <table className="min-w-full divide-y divide-white/8 text-left">
                        <thead className="bg-white/[0.03]">
                          <tr className="text-xs uppercase tracking-[0.24em] text-zinc-500">
                            <th className="px-4 py-3 font-medium">Ingredient</th>
                            <th className="px-4 py-3 font-medium">Location</th>
                            <th className="px-4 py-3 font-medium">Actual</th>
                            <th className="px-4 py-3 font-medium">Theory</th>
                            <th className="px-4 py-3 font-medium">Gap</th>
                            <th className="px-4 py-3 font-medium">Benchmark</th>
                            <th className="px-4 py-3 font-medium">Issue</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-white/6 bg-black/10">
                          {{marginResponse.data.rows.map((row) => (
                            <tr
                              key={{row.ingredientId}}
                              onClick={{() => setSelectedIngredientId(row.ingredientId)}}
                              className={{`cursor-pointer transition hover:bg-white/[0.04] ${'{'}activeId === row.ingredientId ? 'bg-emerald-400/8' : ''{'}'}`}}
                            >
                              <td className="px-4 py-4">
                                <div>
                                  <p className="font-medium text-white">{{row.ingredient}}</p>
                                  <p className="mt-1 text-xs text-zinc-500">{{row.category}} · {{row.vendor}}</p>
                                </div>
                              </td>
                              <td className="px-4 py-4 text-sm text-zinc-300">{{row.location}}</td>
                              <td className="px-4 py-4 font-mono text-sm text-white">${'${'}row.actualCost.toFixed(2){'}'}</td>
                              <td className="px-4 py-4 font-mono text-sm text-zinc-300">${'${'}row.theoreticalCost.toFixed(2){'}'}</td>
                              <td className="px-4 py-4 font-mono text-sm text-red-300">{{formatPercent(row.gapPct)}}</td>
                              <td className="px-4 py-4 font-mono text-sm text-cyan-200">{{formatPercent(row.benchmarkPct)}}</td>
                              <td className="px-4 py-4 text-sm text-zinc-400">{{row.issue}}</td>
                            </tr>
                          ))}}
                        </tbody>
                      </table>
                    </div>
                  </div>
                </Surface>

                <div className="space-y-6">
                  <Surface>
                    <SectionHeading
                      eyebrow="Overlay"
                      title="Benchmark context"
                      description="This overlay keeps the operator focused on outliers that are materially beyond portfolio and peer ranges."
                    />
                    <div className="mt-6 h-64">
                      <DonutChart
                        className="mx-auto h-60"
                        data={{overlayData}}
                        category="value"
                        index="name"
                        colors={{['rose', 'cyan', 'emerald']}}
                        valueFormatter={{(value) => `${{value}} pts`}}
                      />
                    </div>
                  </Surface>

                  <Surface>
                    <SectionHeading
                      eyebrow="Drill-down"
                      title={{drilldownResponse.data.ingredient}}
                      description={{drilldownResponse.data.story}}
                    />
                    <div className="mt-6 grid gap-3 md:grid-cols-3">
                      <div className="rounded-2xl border border-white/8 bg-white/[0.03] p-4">
                        <p className="text-xs uppercase tracking-[0.24em] text-zinc-500">Invoice delta</p>
                        <p className="mt-2 font-mono text-xl text-red-300">{{drilldownResponse.data.invoiceDelta}}</p>
                      </div>
                      <div className="rounded-2xl border border-white/8 bg-white/[0.03] p-4">
                        <p className="text-xs uppercase tracking-[0.24em] text-zinc-500">Yield delta</p>
                        <p className="mt-2 font-mono text-xl text-amber-200">{{drilldownResponse.data.yieldDelta}}</p>
                      </div>
                      <div className="rounded-2xl border border-white/8 bg-white/[0.03] p-4">
                        <p className="text-xs uppercase tracking-[0.24em] text-zinc-500">Benchmark delta</p>
                        <p className="mt-2 font-mono text-xl text-cyan-200">{{drilldownResponse.data.benchmarkDelta}}</p>
                      </div>
                    </div>
                    <div className="mt-6 h-64">
                      <BarChart
                        className="h-64"
                        data={{drilldownResponse.data.events}}
                        index="label"
                        categories={{['value']}}
                        colors={{['emerald']}}
                        showLegend={{false}}
                        valueFormatter={{(value) => `${{value}}`}}
                        yAxisWidth={{56}}
                      />
                    </div>
                  </Surface>
                </div>
              </section>
            </div>
          );
        }}
    '''),
    client / 'pages' / 'ReorderPage.tsx': dedent('''
        /**
         * Design reminder: treat reorder suggestions like an operator queue—dense, directional, and anchored by risk color rather than decorative elements.
         */
        import { useCallback } from 'react';
        import { api } from '@/services/api';
        import { reorderData } from '@/data/mockData';
        import { useFetch } from '@/hooks/useFetch';
        import {
          LoadingPanel,
          PageStateBanner,
          SectionHeading,
          SeverityBadge,
          Surface,
        } from '@/components/dashboard-primitives';

        export default function ReorderPage() {
          const fetchReorders = useCallback(() => api.getReorderSuggestions(), []);
          const { data, loading, error, usingFallback } = useFetch(fetchReorders, { fallbackData: reorderData });

          if (loading) return <LoadingPanel label="Calculating reorder queue…" />;

          return (
            <div className="space-y-6">
              <Surface className="overflow-hidden p-0">
                <div className="grid gap-0 xl:grid-cols-[1.1fr_0.9fr]">
                  <div className="p-6 sm:p-8">
                    <SectionHeading
                      eyebrow="Smart replenishment"
                      title="Reorder suggestions with exhaustion timing"
                      description="The reorder queue combines on-hand levels, projected depletion, and alternate vendor economics so buyers can choose timing and source without leaving the command center."
                    />
                  </div>
                  <div className="border-t border-white/8 bg-white/[0.03] p-6 xl:border-l xl:border-t-0">
                    <p className="font-mono text-[11px] uppercase tracking-[0.28em] text-zinc-500">What the operator sees</p>
                    <p className="mt-3 text-sm leading-7 text-zinc-300">Back Bay mozzarella and South End chicken are both nearing exhaustion. The best demo move is to show how alternate vendor pricing protects the next order while preventing emergency buys.</p>
                  </div>
                </div>
              </Surface>

              <PageStateBanner usingFallback={usingFallback} error={error} />

              <section className="grid gap-6 xl:grid-cols-[1.15fr_0.85fr]">
                <Surface>
                  <SectionHeading
                    eyebrow="Queue"
                    title="Suggested orders"
                    description="Critical rows should be addressed first to avoid rush buys and menu disruptions."
                  />
                  <div className="mt-6 overflow-hidden rounded-[28px] border border-white/8">
                    <div className="overflow-x-auto">
                      <table className="min-w-full divide-y divide-white/8">
                        <thead className="bg-white/[0.03] text-left text-xs uppercase tracking-[0.24em] text-zinc-500">
                          <tr>
                            <th className="px-4 py-3 font-medium">Ingredient</th>
                            <th className="px-4 py-3 font-medium">Location</th>
                            <th className="px-4 py-3 font-medium">On hand</th>
                            <th className="px-4 py-3 font-medium">Exhaustion</th>
                            <th className="px-4 py-3 font-medium">Suggested order</th>
                            <th className="px-4 py-3 font-medium">Vendor</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-white/6 bg-black/10">
                          {data.suggestions.map((row) => (
                            <tr key={row.sku} className="transition hover:bg-white/[0.04]">
                              <td className="px-4 py-4">
                                <div>
                                  <p className="font-medium text-white">{row.ingredient}</p>
                                  <p className="mt-1 font-mono text-xs text-zinc-500">{row.sku}</p>
                                </div>
                              </td>
                              <td className="px-4 py-4 text-sm text-zinc-300">{row.location}</td>
                              <td className="px-4 py-4 font-mono text-sm text-zinc-200">{row.onHand}</td>
                              <td className="px-4 py-4 text-sm text-zinc-300">{row.projectedExhaustion}</td>
                              <td className="px-4 py-4 font-mono text-sm text-emerald-300">{row.suggestedOrder}</td>
                              <td className="px-4 py-4">
                                <p className="text-sm text-white">{row.alternateVendor}</p>
                                <p className="mt-1 font-mono text-xs text-zinc-500">{row.vendorBestPrice}</p>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                </Surface>

                <Surface>
                  <SectionHeading
                    eyebrow="Inventory posture"
                    title="Par versus on-hand"
                    description="A compact readiness view for the most watched ingredients across the fleet."
                  />
                  <div className="mt-6 space-y-4">
                    {data.inventoryLevels.map((item) => {
                      const ratio = Math.max(0, Math.min(100, (item.onHand / item.parLevel) * 100));
                      return (
                        <div key={`${item.location}-${item.ingredient}`} className="rounded-3xl border border-white/8 bg-white/[0.03] p-4">
                          <div className="flex flex-wrap items-center justify-between gap-3">
                            <div>
                              <p className="font-medium text-white">{item.ingredient}</p>
                              <p className="mt-1 text-sm text-zinc-500">{item.location}</p>
                            </div>
                            <SeverityBadge severity={ratio < 45 ? 'critical' : ratio < 70 ? 'watch' : 'stable'} />
                          </div>
                          <div className="mt-4 h-2 overflow-hidden rounded-full bg-white/8">
                            <div className="h-full rounded-full bg-gradient-to-r from-emerald-400 to-cyan-300" style={{ width: `${ratio}%` }} />
                          </div>
                          <div className="mt-3 flex items-center justify-between font-mono text-xs uppercase tracking-[0.24em] text-zinc-500">
                            <span>On hand {item.onHand}</span>
                            <span>Par {item.parLevel}</span>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </Surface>
              </section>
            </div>
          );
        }
    '''),
    client / 'pages' / 'VendorsPage.tsx': dedent('''
        /**
         * Design reminder: vendor view should feel networked and comparative, with drift detection elevated over decorative summary cards.
         */
        import {{ LineChart }} from '@tremor/react';
        import {{ useCallback }} from 'react';
        import {{ api }} from '@/services/api';
        import {{ vendorData }} from '@/data/mockData';
        import {{ useFetch }} from '@/hooks/useFetch';
        import {{ HeroPanel, LoadingPanel, PageStateBanner, SectionHeading, SeverityBadge, Surface }} from '@/components/dashboard-primitives';

        export default function VendorsPage() {{
          const fetchVendors = useCallback(() => api.getVendorsScorecard(), []);
          const {{ data, loading, error, usingFallback }} = useFetch(fetchVendors, {{ fallbackData: vendorData }});

          if (loading) return <LoadingPanel label="Loading vendor network intelligence…" />;

          return (
            <div className="space-y-6">
              <HeroPanel
                eyebrow="Vendor network"
                title="Scorecards, price drift, and supplier accountability"
                description="The vendor scorecard keeps service quality and cost discipline in the same frame. Drift detection is what turns a static supplier report into a procurement control system."
                image="https://d2xsxph8kpxj0f.cloudfront.net/310519663540603382/KRgpskTa3UjstPtv6w78ES/hostgraph-vendor-network-4gKUJ8bWcc6RN7G3PScBaC.webp"
              >
                <Surface className="bg-black/20">
                  <p className="font-mono text-[11px] uppercase tracking-[0.28em] text-zinc-500">Current headline</p>
                  <p className="mt-3 text-sm leading-7 text-zinc-300">Sysco service remains acceptable, but invoice accuracy is the weakest in the fleet because mozzarella pricing drift continues after the catalog refresh.</p>
                </Surface>
              </HeroPanel>

              <PageStateBanner usingFallback={{usingFallback}} error={{error}} />

              <section className="grid gap-6 xl:grid-cols-[0.95fr_1.05fr]">
                <Surface>
                  <SectionHeading
                    eyebrow="Scorecard"
                    title="Vendor comparison"
                    description="Service metrics and price discipline are shown together so the buyer can separate reliable vendors from expensive ones."
                  />
                  <div className="mt-6 space-y-4">
                    {{data.scorecard.map((vendorRow) => (
                      <div key={{vendorRow.vendor}} className="rounded-3xl border border-white/8 bg-white/[0.03] p-4">
                        <div className="flex flex-wrap items-start justify-between gap-3">
                          <div>
                            <h4 className="text-lg font-medium text-white">{{vendorRow.vendor}}</h4>
                            <p className="mt-2 text-sm leading-6 text-zinc-400">{{vendorRow.note}}</p>
                          </div>
                          <SeverityBadge severity={{vendorRow.priceDriftPct > 8 ? 'critical' : vendorRow.priceDriftPct > 5 ? 'warning' : 'info'}} />
                        </div>
                        <div className="mt-5 grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
                          <div className="rounded-2xl border border-white/8 bg-black/20 p-3"><p className="text-xs uppercase tracking-[0.24em] text-zinc-500">On time</p><p className="mt-2 font-mono text-xl text-white">{{vendorRow.onTimePct}}%</p></div>
                          <div className="rounded-2xl border border-white/8 bg-black/20 p-3"><p className="text-xs uppercase tracking-[0.24em] text-zinc-500">Fill rate</p><p className="mt-2 font-mono text-xl text-white">{{vendorRow.fillRatePct}}%</p></div>
                          <div className="rounded-2xl border border-white/8 bg-black/20 p-3"><p className="text-xs uppercase tracking-[0.24em] text-zinc-500">Price drift</p><p className="mt-2 font-mono text-xl text-red-300">{{vendorRow.priceDriftPct}}%</p></div>
                          <div className="rounded-2xl border border-white/8 bg-black/20 p-3"><p className="text-xs uppercase tracking-[0.24em] text-zinc-500">Invoice accuracy</p><p className="mt-2 font-mono text-xl text-cyan-200">{{vendorRow.invoiceAccuracyPct}}%</p></div>
                        </div>
                      </div>
                    ))}}
                  </div>
                </Surface>

                <div className="space-y-6">
                  <Surface>
                    <SectionHeading
                      eyebrow="Price trend"
                      title="Commodity trendlines"
                      description="Mozzarella is the standout anomaly in the demo because it decouples from the rest of the ingredient basket while service metrics stay relatively stable."
                    />
                    <div className="mt-6 h-80">
                      <LineChart
                        className="h-80"
                        data={{data.priceTrends}}
                        index="month"
                        categories={{['mozzarella', 'chicken', 'avocados']}}
                        colors={{['rose', 'emerald', 'cyan']}}
                        yAxisWidth={{56}}
                        valueFormatter={{(value) => `$${{value}}`}}
                      />
                    </div>
                  </Surface>

                  <Surface>
                    <SectionHeading
                      eyebrow="Drift feed"
                      title="Supplier alerts"
                      description="These notices are meant to trigger negotiation, credit recovery, or buy-shift decisions."
                    />
                    <div className="mt-6 space-y-4">
                      {{data.driftAlerts.map((alert) => (
                        <div key={{alert.id}} className="rounded-3xl border border-white/8 bg-white/[0.03] p-4">
                          <div className="flex items-center justify-between gap-3">
                            <h4 className="font-medium text-white">{{alert.title}}</h4>
                            <SeverityBadge severity={{alert.severity}} />
                          </div>
                          <p className="mt-3 text-sm leading-6 text-zinc-400">{{alert.detail}}</p>
                          <p className="mt-3 font-mono text-[11px] uppercase tracking-[0.24em] text-zinc-500">{{alert.location}} · {{alert.timestamp}}</p>
                        </div>
                      ))}}
                    </div>
                  </Surface>
                </div>
              </section>
            </div>
          );
        }}
    '''),
    client / 'pages' / 'ShrinkagePage.tsx': dedent('''
        /**
         * Design reminder: shrinkage view should feel diagnostic and operational, using yield deltas and loss values as the primary hierarchy.
         */
        import { BarChart } from '@tremor/react';
        import { useCallback } from 'react';
        import { api } from '@/services/api';
        import { shrinkageData } from '@/data/mockData';
        import { useFetch } from '@/hooks/useFetch';
        import {
          formatCurrencyCompact,
          HeroPanel,
          LoadingPanel,
          MetricCard,
          PageStateBanner,
          SectionHeading,
          Surface,
        } from '@/components/dashboard-primitives';

        export default function ShrinkagePage() {
          const fetchShrinkage = useCallback(() => api.getShrinkageReport(), []);
          const { data, loading, error, usingFallback } = useFetch(fetchShrinkage, { fallbackData: shrinkageData });

          if (loading) return <LoadingPanel label="Loading shrinkage and yield report…" />;

          return (
            <div className="space-y-6">
              <Surface className="overflow-hidden p-0">
                <div className="grid gap-0 xl:grid-cols-[1.1fr_0.9fr]">
                  <div className="p-6 sm:p-8">
                    <SectionHeading
                      eyebrow="Yield discipline"
                      title="Expected versus actual output by location"
                      description="Shrinkage is where the command center proves it can separate supplier problems from kitchen execution. Chicken trim in South End remains the clearest operational demo moment."
                    />
                  </div>
                  <div className="border-t border-white/8 bg-white/[0.03] p-6 xl:border-l xl:border-t-0">
                    <p className="font-mono text-[11px] uppercase tracking-[0.28em] text-zinc-500">Interpretation</p>
                    <p className="mt-3 text-sm leading-7 text-zinc-300">Negative yield variance pushes effective plate cost higher even when invoice pricing stays stable. That distinction helps the operator act on training, prep process, or receiving discipline.</p>
                  </div>
                </div>
              </Surface>

              <PageStateBanner usingFallback={usingFallback} error={error} />

              <section className="grid gap-4 xl:grid-cols-2">
                {data.summary.map((item) => (
                  <MetricCard key={item.title} {...item} />
                ))}
              </section>

              <section className="grid gap-6 xl:grid-cols-[1.05fr_0.95fr]">
                <Surface>
                  <SectionHeading
                    eyebrow="Loss table"
                    title="Location comparison"
                    description="Rows are sorted by avoidable dollar loss so operators can prioritize intervention."
                  />
                  <div className="mt-6 overflow-hidden rounded-[28px] border border-white/8">
                    <div className="overflow-x-auto">
                      <table className="min-w-full divide-y divide-white/8">
                        <thead className="bg-white/[0.03] text-left text-xs uppercase tracking-[0.24em] text-zinc-500">
                          <tr>
                            <th className="px-4 py-3 font-medium">Location</th>
                            <th className="px-4 py-3 font-medium">Ingredient</th>
                            <th className="px-4 py-3 font-medium">Expected yield</th>
                            <th className="px-4 py-3 font-medium">Actual yield</th>
                            <th className="px-4 py-3 font-medium">Variance</th>
                            <th className="px-4 py-3 font-medium">Loss</th>
                          </tr>
                        </thead>
                        <tbody className="divide-y divide-white/6 bg-black/10">
                          {data.rows.map((row) => (
                            <tr key={`${row.location}-${row.ingredient}`} className="transition hover:bg-white/[0.04]">
                              <td className="px-4 py-4 text-sm text-white">{row.location}</td>
                              <td className="px-4 py-4 text-sm text-zinc-300">{row.ingredient}</td>
                              <td className="px-4 py-4 font-mono text-sm text-zinc-200">{row.expectedYield.toFixed(1)}%</td>
                              <td className="px-4 py-4 font-mono text-sm text-zinc-200">{row.actualYield.toFixed(1)}%</td>
                              <td className="px-4 py-4 font-mono text-sm text-red-300">{row.variancePct.toFixed(1)}%</td>
                              <td className="px-4 py-4 font-mono text-sm text-white">{formatCurrencyCompact(row.lossValue)}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                </Surface>

                <Surface>
                  <SectionHeading
                    eyebrow="Yield spread"
                    title="Avoidable loss by ingredient"
                    description="The bar view makes it obvious that chicken and avocado handling deserve the next operational pass."
                  />
                  <div className="mt-6 h-80">
                    <BarChart
                      className="h-80"
                      data={data.rows.map((row) => ({ ingredient: `${row.location} · ${row.ingredient}`, lossValue: row.lossValue }))}
                      index="ingredient"
                      categories={['lossValue']}
                      colors={['rose']}
                      showLegend={false}
                      valueFormatter={formatCurrencyCompact}
                      yAxisWidth={64}
                    />
                  </div>
                </Surface>
              </section>
            </div>
          );
        }
    '''),
    client / 'pages' / 'AlertsPage.tsx': dedent('''
        /**
         * Design reminder: alerts should read like an operations pulse wall—severity first, compact narrative second, with strong contrast against the dark surface.
         */
        import {{ useCallback }} from 'react';
        import {{ api }} from '@/services/api';
        import {{ alertsData }} from '@/data/mockData';
        import {{ useFetch }} from '@/hooks/useFetch';
        import {{ HeroPanel, LoadingPanel, PageStateBanner, SectionHeading, SeverityBadge, Surface }} from '@/components/dashboard-primitives';

        export default function AlertsPage() {{
          const fetchAlerts = useCallback(() => api.getAlerts(), []);
          const {{ data, loading, error, usingFallback }} = useFetch(fetchAlerts, {{ fallbackData: alertsData }});

          if (loading) return <LoadingPanel label="Syncing active alert feed…" />;

          return (
            <div className="space-y-6">
              <HeroPanel
                eyebrow="Alert pulse"
                title="Every active anomaly in one feed"
                description="The alert wall keeps the operator oriented around exceptions instead of averages. Use it as the opening frame when you want the story to start with urgency."
                image="https://d2xsxph8kpxj0f.cloudfront.net/310519663540603382/KRgpskTa3UjstPtv6w78ES/hostgraph-alerts-pulse-ATNXMeoLi5seV6giqm5WfA.webp"
              >
                <Surface className="bg-black/20">
                  <p className="font-mono text-[11px] uppercase tracking-[0.28em] text-zinc-500">Current pulse</p>
                  <p className="mt-3 text-sm leading-7 text-zinc-300">There are {{data.alerts.filter((item) => item.severity === 'critical').length}} critical signals in the queue. The strongest opener remains the mozzarella overbilling cluster across the Boston portfolio.</p>
                </Surface>
              </HeroPanel>

              <PageStateBanner usingFallback={{usingFallback}} error={{error}} />

              <Surface>
                <SectionHeading
                  eyebrow="Feed"
                  title="Active alerts"
                  description="Alerts combine procurement, inventory, and operational anomalies so the buyer sees the full consequence chain in one stream."
                />
                <div className="mt-6 space-y-4">
                  {{data.alerts.map((alert) => (
                    <div key={{alert.id}} className="rounded-[28px] border border-white/8 bg-gradient-to-r from-white/[0.04] to-white/[0.02] p-5">
                      <div className="flex flex-wrap items-start justify-between gap-4">
                        <div>
                          <h4 className="text-lg font-medium text-white">{{alert.title}}</h4>
                          <p className="mt-3 max-w-3xl text-sm leading-7 text-zinc-400">{{alert.detail}}</p>
                        </div>
                        <SeverityBadge severity={{alert.severity}} />
                      </div>
                      <div className="mt-4 flex flex-wrap gap-4 font-mono text-[11px] uppercase tracking-[0.24em] text-zinc-500">
                        <span>{{alert.location}}</span>
                        <span>{{alert.timestamp}}</span>
                      </div>
                    </div>
                  ))}}
                </div>
              </Surface>
            </div>
          );
        }}
    '''),
    client / 'pages' / 'Home.tsx': dedent('''
        /**
         * Design reminder: home route should land directly in the dashboard command surface with no generic landing-page detour.
         */
        export { default } from './DashboardPage';
    '''),
    client / 'pages' / 'DashboardPage.tsx.placeholder': '',
    client / 'pages' / 'NotFound.tsx': dedent('''
        /**
         * Design reminder: even failure states should preserve the command-center tone and provide a clear escape route.
         */
        import { Link } from 'react-router-dom';
        import { Surface } from '@/components/dashboard-primitives';

        export default function NotFound() {
          return (
            <div className="flex min-h-screen items-center justify-center bg-background px-6">
              <Surface className="max-w-xl text-center">
                <p className="font-mono text-[11px] uppercase tracking-[0.32em] text-zinc-500">404 · lost in the graph</p>
                <h1 className="mt-4 text-4xl font-semibold text-white">This route is outside the command center.</h1>
                <p className="mt-4 text-sm leading-7 text-zinc-400">
                  The requested screen is not part of the current HostGraph build. Return to the dashboard summary to continue exploring the procurement workflow.
                </p>
                <Link
                  to="/"
                  className="mt-8 inline-flex rounded-full border border-emerald-400/20 bg-emerald-400/10 px-5 py-3 text-sm font-medium text-emerald-100 transition hover:bg-emerald-400/16"
                >
                  Return to dashboard summary
                </Link>
              </Surface>
            </div>
          );
        }
    '''),
    client / 'App.tsx': dedent('''
        /**
         * Design reminder: the whole app follows the industrial neo-noir command-center philosophy with a persistent left rail and dark analytical surfaces.
         */
        import { Toaster } from '@/components/ui/sonner';
        import { TooltipProvider } from '@/components/ui/tooltip';
        import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
        import ErrorBoundary from './components/ErrorBoundary';
        import { HostGraphShell } from './components/HostGraphShell';
        import { ThemeProvider } from './contexts/ThemeContext';
        import AlertsPage from './pages/AlertsPage';
        import DashboardPage from './pages/DashboardPage';
        import MarginGapPage from './pages/MarginGapPage';
        import NotFound from './pages/NotFound';
        import ReorderPage from './pages/ReorderPage';
        import ShrinkagePage from './pages/ShrinkagePage';
        import VendorsPage from './pages/VendorsPage';

        function AppRouter() {
          return (
            <BrowserRouter>
              <Routes>
                <Route element={<HostGraphShell />}>
                  <Route path="/" element={<DashboardPage />} />
                  <Route path="/margin-gap" element={<MarginGapPage />} />
                  <Route path="/reorder" element={<ReorderPage />} />
                  <Route path="/vendors" element={<VendorsPage />} />
                  <Route path="/shrinkage" element={<ShrinkagePage />} />
                  <Route path="/alerts" element={<AlertsPage />} />
                  <Route path="/home" element={<Navigate to="/" replace />} />
                </Route>
                <Route path="*" element={<NotFound />} />
              </Routes>
            </BrowserRouter>
          );
        }

        export default function App() {
          return (
            <ErrorBoundary>
              <ThemeProvider defaultTheme="dark">
                <TooltipProvider>
                  <Toaster />
                  <AppRouter />
                </TooltipProvider>
              </ThemeProvider>
            </ErrorBoundary>
          );
        }
    '''),
    client / 'index.css': dedent('''
        /**
         * Design reminder: industrial neo-noir control room; dark slate field, emerald/cyan guidance, red for leakage only, with refined typography and texture.
         */
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
        @import 'tailwindcss';
        @import 'tw-animate-css';

        @custom-variant dark (&:is(.dark *));

        @theme inline {
          --radius-sm: calc(var(--radius) - 4px);
          --radius-md: calc(var(--radius) - 2px);
          --radius-lg: var(--radius);
          --radius-xl: calc(var(--radius) + 4px);
          --color-background: var(--background);
          --color-foreground: var(--foreground);
          --color-card: var(--card);
          --color-card-foreground: var(--card-foreground);
          --color-popover: var(--popover);
          --color-popover-foreground: var(--popover-foreground);
          --color-primary: var(--primary);
          --color-primary-foreground: var(--primary-foreground);
          --color-secondary: var(--secondary);
          --color-secondary-foreground: var(--secondary-foreground);
          --color-muted: var(--muted);
          --color-muted-foreground: var(--muted-foreground);
          --color-accent: var(--accent);
          --color-accent-foreground: var(--accent-foreground);
          --color-destructive: var(--destructive);
          --color-destructive-foreground: var(--destructive-foreground);
          --color-border: var(--border);
          --color-input: var(--input);
          --color-ring: var(--ring);
          --color-chart-1: var(--chart-1);
          --color-chart-2: var(--chart-2);
          --color-chart-3: var(--chart-3);
          --color-chart-4: var(--chart-4);
          --color-chart-5: var(--chart-5);
          --color-sidebar: var(--sidebar);
          --color-sidebar-foreground: var(--sidebar-foreground);
          --color-sidebar-primary: var(--sidebar-primary);
          --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
          --color-sidebar-accent: var(--sidebar-accent);
          --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
          --color-sidebar-border: var(--sidebar-border);
          --color-sidebar-ring: var(--sidebar-ring);
          --font-sans: 'IBM Plex Sans', ui-sans-serif, system-ui, sans-serif;
          --font-mono: 'IBM Plex Mono', ui-monospace, monospace;
        }

        :root {
          --radius: 1rem;
          --background: oklch(0.16 0.015 270);
          --foreground: oklch(0.92 0.01 265);
          --card: oklch(0.2 0.015 272);
          --card-foreground: oklch(0.92 0.01 265);
          --popover: oklch(0.2 0.015 272);
          --popover-foreground: oklch(0.92 0.01 265);
          --primary: oklch(0.75 0.15 162);
          --primary-foreground: oklch(0.12 0.01 265);
          --secondary: oklch(0.26 0.018 270);
          --secondary-foreground: oklch(0.88 0.01 265);
          --muted: oklch(0.24 0.015 270);
          --muted-foreground: oklch(0.68 0.012 270);
          --accent: oklch(0.24 0.02 250);
          --accent-foreground: oklch(0.9 0.01 260);
          --destructive: oklch(0.65 0.2 25);
          --destructive-foreground: oklch(0.97 0 0);
          --border: oklch(0.36 0.01 270 / 0.34);
          --input: oklch(0.34 0.01 270 / 0.44);
          --ring: oklch(0.72 0.14 162 / 0.7);
          --chart-1: oklch(0.76 0.15 162);
          --chart-2: oklch(0.74 0.12 227);
          --chart-3: oklch(0.74 0.17 25);
          --chart-4: oklch(0.65 0.18 340);
          --chart-5: oklch(0.82 0.13 88);
          --sidebar: oklch(0.17 0.012 270);
          --sidebar-foreground: oklch(0.92 0.01 265);
          --sidebar-primary: oklch(0.75 0.15 162);
          --sidebar-primary-foreground: oklch(0.12 0.01 265);
          --sidebar-accent: oklch(0.26 0.018 270);
          --sidebar-accent-foreground: oklch(0.92 0.01 265);
          --sidebar-border: oklch(0.36 0.01 270 / 0.34);
          --sidebar-ring: oklch(0.72 0.14 162 / 0.7);
        }

        .dark {
          --background: oklch(0.16 0.015 270);
          --foreground: oklch(0.92 0.01 265);
          --card: oklch(0.2 0.015 272);
          --card-foreground: oklch(0.92 0.01 265);
          --popover: oklch(0.2 0.015 272);
          --popover-foreground: oklch(0.92 0.01 265);
          --primary: oklch(0.75 0.15 162);
          --primary-foreground: oklch(0.12 0.01 265);
          --secondary: oklch(0.26 0.018 270);
          --secondary-foreground: oklch(0.88 0.01 265);
          --muted: oklch(0.24 0.015 270);
          --muted-foreground: oklch(0.68 0.012 270);
          --accent: oklch(0.24 0.02 250);
          --accent-foreground: oklch(0.9 0.01 260);
          --destructive: oklch(0.65 0.2 25);
          --destructive-foreground: oklch(0.97 0 0);
          --border: oklch(0.36 0.01 270 / 0.34);
          --input: oklch(0.34 0.01 270 / 0.44);
          --ring: oklch(0.72 0.14 162 / 0.7);
          --chart-1: oklch(0.76 0.15 162);
          --chart-2: oklch(0.74 0.12 227);
          --chart-3: oklch(0.74 0.17 25);
          --chart-4: oklch(0.65 0.18 340);
          --chart-5: oklch(0.82 0.13 88);
          --sidebar: oklch(0.17 0.012 270);
          --sidebar-foreground: oklch(0.92 0.01 265);
          --sidebar-primary: oklch(0.75 0.15 162);
          --sidebar-primary-foreground: oklch(0.12 0.01 265);
          --sidebar-accent: oklch(0.26 0.018 270);
          --sidebar-accent-foreground: oklch(0.92 0.01 265);
          --sidebar-border: oklch(0.36 0.01 270 / 0.34);
          --sidebar-ring: oklch(0.72 0.14 162 / 0.7);
        }

        @layer base {
          * {
            @apply border-border outline-ring/50;
          }

          html {
            @apply dark;
          }

          body {
            @apply bg-background text-foreground font-sans antialiased;
            background-image: linear-gradient(to bottom, rgba(255,255,255,0.03), rgba(255,255,255,0)), radial-gradient(circle at top, rgba(16,185,129,0.08), transparent 26%);
            min-height: 100vh;
          }

          h1,
          h2,
          h3,
          h4,
          h5,
          h6 {
            font-family: 'Space Grotesk', var(--font-sans);
          }

          button:not(:disabled),
          [role='button']:not([aria-disabled='true']),
          [type='button']:not(:disabled),
          [type='submit']:not(:disabled),
          [type='reset']:not(:disabled),
          a[href],
          select:not(:disabled),
          input:not(:disabled),
          textarea:not(:disabled) {
            @apply cursor-pointer;
          }
        }

        @layer components {
          .container {
            width: 100%;
            margin-left: auto;
            margin-right: auto;
            padding-left: 1rem;
            padding-right: 1rem;
          }

          .flex {
            min-height: 0;
            min-width: 0;
          }

          @media (min-width: 640px) {
            .container {
              padding-left: 1.5rem;
              padding-right: 1.5rem;
            }
          }

          @media (min-width: 1024px) {
            .container {
              padding-left: 2rem;
              padding-right: 2rem;
              max-width: 1360px;
            }
          }
        }
    '''),
    root / 'client' / 'index.html': dedent('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1" />
            <title>HostGraph Procurement Command Center</title>
            <meta
              name="description"
              content="HostGraph is a procurement command center for restaurant operators, connecting live backend analytics with a standalone demo mode backed by mock data."
            />
          </head>
          <body>
            <div id="root"></div>
            <script type="module" src="/src/main.tsx"></script>
            <script
              defer
              src="%VITE_ANALYTICS_ENDPOINT%/umami"
              data-website-id="%VITE_ANALYTICS_WEBSITE_ID%"></script>
          </body>
        </html>
    '''),
    root / 'README.md': dedent('''
        # HostGraph Procurement Command Center

        HostGraph is a dark-mode procurement intelligence frontend for restaurant operators. The app includes six views—Dashboard Summary, Margin Gap Report, Reorder Suggestions, Vendor Scorecard, Shrinkage & Yield, and Alerts—and is designed to connect to a backend API while still working as a standalone demo.

        ## Design direction

        The chosen design philosophy is an **industrial neo-noir command center**: deep slate and zinc surfaces, restrained emerald and red accents, a persistent left rail, and dense but legible information hierarchy. Typography combines **Space Grotesk** for headings with **IBM Plex Sans** and **IBM Plex Mono** for operational detail.

        ## Views

        | Route | View | Purpose |
        | --- | --- | --- |
        | `/` | Dashboard Summary | KPI cards, leaking ingredients, benchmark mix, action items |
        | `/margin-gap` | Margin Gap Report | Hero analytical view with filters, cost table, benchmark overlay, drill-down |
        | `/reorder` | Reorder Suggestions | Suggested buys, exhaustion timing, and inventory posture |
        | `/vendors` | Vendor Scorecard | Supplier comparison, price trends, and drift alerts |
        | `/shrinkage` | Shrinkage & Yield | Yield variance and avoidable loss by location |
        | `/alerts` | Alerts | Active alert feed for procurement and operational anomalies |

        ## API integration

        The frontend wraps these endpoints in `client/src/services/api.ts`:

        | Method | Endpoint |
        | --- | --- |
        | GET | `/api/v1/dashboard/summary` |
        | GET | `/api/v1/margin-gap` |
        | GET | `/api/v1/margin-gap/:ingredientId/drilldown` |
        | GET | `/api/v1/inventory/levels` |
        | GET | `/api/v1/inventory/reorder-suggestions` |
        | GET | `/api/v1/shrinkage-report` |
        | GET | `/api/v1/benchmarks` |
        | GET | `/api/v1/vendors/scorecard` |
        | GET | `/api/v1/price-trends` |
        | GET | `/api/v1/alerts` |
        | POST | `/api/v1/invoices/upload` |

        All page-level data access goes through `client/src/hooks/useFetch.ts`. The hook manages loading and error state, then gracefully falls back to `client/src/data/mockData.ts` whenever the API is unavailable.

        ## Running connected to the backend

        1. Start the backend API locally on **`http://localhost:3000`**.
        2. Start the frontend dev server:

        ```bash
        pnpm install
        pnpm dev
        ```

        The Vite dev server runs on **`http://localhost:5173`** and proxies any `/api` request to `http://localhost:3000`.

        ## Running standalone with mock data

        If the backend is not running, start the frontend normally:

        ```bash
        pnpm install
        pnpm dev
        ```

        The app will attempt to call the API first. If those requests fail, each page automatically falls back to the built-in Boston restaurant-group mock data, including the demo “gotcha” stories around Sysco overbilling, chicken yield variance, and mozzarella price gouging.

        ## Build and verification

        Use the following commands to verify the app compiles cleanly:

        ```bash
        pnpm check
        pnpm build
        ```
    '''),
    root / 'vite.config.ts': dedent('''
        import { jsxLocPlugin } from '@builder.io/vite-plugin-jsx-loc';
        import tailwindcss from '@tailwindcss/vite';
        import react from '@vitejs/plugin-react';
        import fs from 'node:fs';
        import path from 'node:path';
        import { defineConfig, type Plugin, type ViteDevServer } from 'vite';
        import { vitePluginManusRuntime } from 'vite-plugin-manus-runtime';

        const PROJECT_ROOT = import.meta.dirname;
        const LOG_DIR = path.join(PROJECT_ROOT, '.manus-logs');
        const MAX_LOG_SIZE_BYTES = 1 * 1024 * 1024;
        const TRIM_TARGET_BYTES = Math.floor(MAX_LOG_SIZE_BYTES * 0.6);

        type LogSource = 'browserConsole' | 'networkRequests' | 'sessionReplay';

        function ensureLogDir() {
          if (!fs.existsSync(LOG_DIR)) {
            fs.mkdirSync(LOG_DIR, { recursive: true });
          }
        }

        function trimLogFile(logPath: string, maxSize: number) {
          try {
            if (!fs.existsSync(logPath) || fs.statSync(logPath).size <= maxSize) {
              return;
            }

            const lines = fs.readFileSync(logPath, 'utf-8').split('\n');
            const keptLines: string[] = [];
            let keptBytes = 0;
            for (let i = lines.length - 1; i >= 0; i -= 1) {
              const lineBytes = Buffer.byteLength(`${lines[i]}\n`, 'utf-8');
              if (keptBytes + lineBytes > TRIM_TARGET_BYTES) break;
              keptLines.unshift(lines[i]);
              keptBytes += lineBytes;
            }
            fs.writeFileSync(logPath, keptLines.join('\n'), 'utf-8');
          } catch {
            // ignore trim errors
          }
        }

        function writeToLogFile(source: LogSource, entries: unknown[]) {
          if (entries.length === 0) return;
          ensureLogDir();
          const logPath = path.join(LOG_DIR, `${source}.log`);
          const lines = entries.map((entry) => `[${new Date().toISOString()}] ${JSON.stringify(entry)}`);
          fs.appendFileSync(logPath, `${lines.join('\n')}\n`, 'utf-8');
          trimLogFile(logPath, MAX_LOG_SIZE_BYTES);
        }

        function vitePluginManusDebugCollector(): Plugin {
          return {
            name: 'manus-debug-collector',
            transformIndexHtml(html) {
              if (process.env.NODE_ENV === 'production') return html;
              return {
                html,
                tags: [
                  {
                    tag: 'script',
                    attrs: {
                      src: '/__manus__/debug-collector.js',
                      defer: true,
                    },
                    injectTo: 'head',
                  },
                ],
              };
            },
            configureServer(server: ViteDevServer) {
              server.middlewares.use('/__manus__/logs', (req, res, next) => {
                if (req.method !== 'POST') return next();

                const handlePayload = (payload: any) => {
                  if (payload.consoleLogs?.length) writeToLogFile('browserConsole', payload.consoleLogs);
                  if (payload.networkRequests?.length) writeToLogFile('networkRequests', payload.networkRequests);
                  if (payload.sessionEvents?.length) writeToLogFile('sessionReplay', payload.sessionEvents);
                  res.writeHead(200, { 'Content-Type': 'application/json' });
                  res.end(JSON.stringify({ success: true }));
                };

                const reqBody = (req as { body?: unknown }).body;
                if (reqBody && typeof reqBody === 'object') {
                  try {
                    handlePayload(reqBody);
                  } catch (error) {
                    res.writeHead(400, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify({ success: false, error: String(error) }));
                  }
                  return;
                }

                let body = '';
                req.on('data', (chunk) => {
                  body += chunk.toString();
                });
                req.on('end', () => {
                  try {
                    handlePayload(JSON.parse(body));
                  } catch (error) {
                    res.writeHead(400, { 'Content-Type': 'application/json' });
                    res.end(JSON.stringify({ success: false, error: String(error) }));
                  }
                });
              });
            },
          };
        }

        const plugins = [react(), tailwindcss(), jsxLocPlugin(), vitePluginManusRuntime(), vitePluginManusDebugCollector()];

        export default defineConfig({
          plugins,
          resolve: {
            alias: {
              '@': path.resolve(import.meta.dirname, 'client', 'src'),
              '@shared': path.resolve(import.meta.dirname, 'shared'),
              '@assets': path.resolve(import.meta.dirname, 'attached_assets'),
            },
          },
          envDir: path.resolve(import.meta.dirname),
          root: path.resolve(import.meta.dirname, 'client'),
          build: {
            outDir: path.resolve(import.meta.dirname, 'dist/public'),
            emptyOutDir: true,
          },
          server: {
            port: 5173,
            strictPort: false,
            host: true,
            proxy: {
              '/api': {
                target: 'http://localhost:3000',
                changeOrigin: true,
              },
            },
            allowedHosts: [
              '.manuspre.computer',
              '.manus.computer',
              '.manus-asia.computer',
              '.manuscomputer.ai',
              '.manusvm.computer',
              'localhost',
              '127.0.0.1',
            ],
            fs: {
              strict: true,
              deny: ['**/.*'],
            },
          },
        });
    '''),
}

# Correct the accidental placeholder key if present later.
files.pop(client / 'pages' / 'DashboardPage.tsx.placeholder')

for path, content in files.items():
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + '\n', encoding='utf-8')
