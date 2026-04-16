/**
 * Design reminder: industrial neo-noir command rail with asymmetrical layout, luminous dividers, and disciplined typography.
 */
import { cn } from '@/lib/utils';
import { prefetchCommonRoutes, prefetchRoute, type PrefetchableRoute } from '@/lib/routePrefetch';
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
import { useEffect } from 'react';
import { NavLink, Outlet } from 'react-router-dom';

const navItems: Array<{ label: string; to: PrefetchableRoute; icon: typeof ChartColumnIncreasing }> = [
  { label: 'Dashboard Summary', to: '/', icon: ChartColumnIncreasing },
  { label: 'Margin Gap Report', to: '/margin-gap', icon: CircleDollarSign },
  { label: 'Reorder Suggestions', to: '/reorder', icon: PackageSearch },
  { label: 'Vendor Scorecard', to: '/vendors', icon: Store },
  { label: 'Shrinkage & Yield', to: '/shrinkage', icon: Wheat },
  { label: 'Alerts', to: '/alerts', icon: BellRing },
];

export function HostGraphShell() {
  useEffect(() => {
    prefetchCommonRoutes(['/margin-gap', '/alerts']);
  }, []);

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
                  onPointerEnter={() => prefetchRoute(to)}
                  onFocus={() => prefetchRoute(to)}
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
