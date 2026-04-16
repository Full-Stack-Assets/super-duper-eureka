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
