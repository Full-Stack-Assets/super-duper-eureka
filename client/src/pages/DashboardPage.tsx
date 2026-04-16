/**
 * Design reminder: industrial neo-noir command-center dashboard with staggered analysis bands and restrained alert accents.
 */
import { DonutChart, BarChart } from '@tremor/react';
import { useCallback } from 'react';
import { api } from '@/services/api';
import { dashboardSummary } from '@/data/mockData';
import { useFetch } from '@/hooks/useFetch';
import {
  formatCurrencyCompact,
  HeroPanel,
  LoadingPanel,
  MetricCard,
  PageStateBanner,
  SectionHeading,
  SeverityBadge,
  Surface,
} from '@/components/dashboard-primitives';

export default function DashboardPage() {
  const fetchDashboard = useCallback(() => api.getDashboardSummary(), []);
  const { data, loading, error, usingFallback } = useFetch(fetchDashboard, { fallbackData: dashboardSummary });

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
            <p className="mt-3 text-sm leading-7 text-zinc-300">{data.narrative}</p>
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

      <PageStateBanner usingFallback={usingFallback} error={error} />

      <section className="grid gap-4 xl:grid-cols-4">
        {data.kpis.map((item) => (
          <MetricCard key={item.title} {...item} />
        ))}
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
              data={data.leakingIngredients}
              index="ingredient"
              categories={['leakage']}
              colors={['emerald']}
              showLegend={false}
              valueFormatter={formatCurrencyCompact}
              yAxisWidth={64}
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
              data={data.benchmarkMix}
              category="value"
              index="name"
              colors={['emerald', 'cyan', 'rose']}
              valueFormatter={(value) => `${value}%`}
            />
            <div className="space-y-4">
              {data.benchmarkMix.map((slice) => (
                <div key={slice.name} className="rounded-2xl border border-white/8 bg-white/[0.03] px-4 py-3">
                  <div className="flex items-center justify-between gap-4">
                    <p className="text-sm text-zinc-300">{slice.name}</p>
                    <span className="font-mono text-base text-white">{slice.value}%</span>
                  </div>
                </div>
              ))}
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
            {data.actions.map((action) => (
              <div key={action.title} className="rounded-3xl border border-white/8 bg-white/[0.03] p-4">
                <div className="flex flex-wrap items-center justify-between gap-3">
                  <h4 className="text-base font-medium text-white">{action.title}</h4>
                  <SeverityBadge severity={action.severity} />
                </div>
                <p className="mt-3 text-sm leading-6 text-zinc-400">{action.description}</p>
                <div className="mt-4 flex flex-wrap items-center gap-4 font-mono text-[11px] uppercase tracking-[0.24em] text-zinc-500">
                  <span>Owner {action.owner}</span>
                  <span>Due {action.due}</span>
                </div>
              </div>
            ))}
          </div>
        </Surface>

        <Surface>
          <SectionHeading
            eyebrow="Bridge"
            title="What is driving the margin gap"
            description="A compact driver bridge that helps the operator separate procurement, waste, and service-level causes."
          />
          <div className="mt-6 grid gap-4 sm:grid-cols-2">
            {data.marginBridge.map((driver) => (
              <div key={driver.label} className="rounded-3xl border border-white/8 bg-gradient-to-br from-white/[0.05] to-white/[0.02] p-5">
                <p className="text-sm text-zinc-400">{driver.label}</p>
                <p className="mt-3 font-mono text-3xl text-white">{formatCurrencyCompact(driver.value)}</p>
              </div>
            ))}
          </div>
        </Surface>
      </section>
    </div>
  );
}
