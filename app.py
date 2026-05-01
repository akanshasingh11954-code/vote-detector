<!doctype html>
<html lang="en" class="h-full bg-black">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Audit • Transparency Ledger</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
      :root { color-scheme: dark; }
      .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }
      .neon { box-shadow: 0 0 0 1px rgba(34,211,238,.35), 0 0 24px rgba(34,211,238,.12); }
    </style>
  </head>
  <body class="h-full text-slate-100">
    <div class="min-h-full bg-gradient-to-b from-black via-slate-950 to-black">
      <div class="mx-auto max-w-5xl px-4 py-10">
        <div class="rounded-2xl border border-cyan-400/30 bg-slate-950/80 p-6 neon">
          <div class="flex items-start justify-between gap-6">
            <div>
              <div class="mono text-cyan-300 text-xs tracking-widest">PUBLIC • TRANSPARENCY LEDGER</div>
              <h1 class="mt-3 text-2xl font-semibold">Audit & Integrity Proof</h1>
              <p class="mt-2 text-slate-300 text-sm leading-relaxed">
                The ledger is publicly visible and hashable. The masked values are readable as bytes,
                but cryptographically meaningless without the aggregate unmasking operation.
              </p>
            </div>
            <div class="flex flex-col sm:flex-row gap-3">
              <a href="/vote" class="inline-flex items-center justify-center rounded-lg border border-cyan-400/40 bg-cyan-400/10 px-4 py-2 mono text-sm text-cyan-200 hover:bg-cyan-400/15 transition">
                Cast Vote
              </a>
              <a href="/admin" class="inline-flex items-center justify-center rounded-lg border border-slate-700 bg-slate-900/40 px-4 py-2 mono text-sm text-slate-200 hover:bg-slate-900/70 transition">
                Admin Vault
              </a>
            </div>
          </div>

          <div class="mt-6 grid gap-4 sm:grid-cols-2">
            <div class="rounded-xl border border-cyan-400/20 bg-black/30 p-5">
              <div class="mono text-xs text-cyan-300">DATABASE SHA‑256</div>
              <div class="mt-2 mono text-sm break-all text-cyan-200">{{ db_hash }}</div>
              <div class="mt-3 text-sm text-slate-300">
                If any byte of <span class="mono">database.txt</span> changes, this hash changes — tampering is detectable.
              </div>
            </div>
            <div class="rounded-xl border border-cyan-400/20 bg-black/30 p-5">
              <div class="mono text-xs text-cyan-300">MASKED_SUM SHA‑256</div>
              <div class="mt-2 mono text-sm break-all text-cyan-200">{{ masked_sum_hash }}</div>
              <div class="mt-3 text-sm text-slate-300">
                A lightweight proof that <span class="mono">masked_sum</span> wasn’t altered between checkpoints.
              </div>
            </div>
          </div>

          <div class="mt-6 rounded-xl border border-cyan-400/20 bg-black/30 p-5">
            <div class="mono text-xs text-cyan-300">WHY INTERNAL LEAKS DON’T REVEAL VOTES</div>
            <ul class="mt-3 space-y-2 text-sm text-slate-300 leading-relaxed">
              <li><span class="mono text-cyan-200">masked_sum</span> is an aggregate of blinded votes: each vote is hidden by unique per‑vote noise.</li>
              <li><span class="mono text-cyan-200">noise_sum</span> is stored only as an aggregate; there is no per‑vote noise record to invert individual votes.</li>
              <li><span class="mono text-cyan-200">hash_list</span> contains only HMAC nullifiers to prevent re‑votes; it does not encode party choice.</li>
              <li>Only the admin operation computes <span class="mono text-cyan-200">(masked_sum - noise_sum) mod PRIME</span> to reveal the final packed tally.</li>
            </ul>
          </div>

          <div class="mt-6 grid gap-4 sm:grid-cols-3">
            <div class="rounded-xl border border-cyan-400/20 bg-black/30 p-5">
              <div class="mono text-xs text-cyan-300">FIELD PRIME</div>
              <div class="mt-2 mono text-sm text-cyan-200 break-all">{{ field_prime }}</div>
            </div>
            <div class="rounded-xl border border-cyan-400/20 bg-black/30 p-5">
              <div class="mono text-xs text-cyan-300">MASKED_SUM (current)</div>
              <div class="mt-2 mono text-sm text-cyan-200 break-all">{{ masked_sum }}</div>
            </div>
            <div class="rounded-xl border border-cyan-400/20 bg-black/30 p-5">
              <div class="mono text-xs text-cyan-300">NULLIFIERS</div>
              <div class="mt-2 mono text-sm text-cyan-200">{{ total_nullifiers }}</div>
            </div>
          </div>

          {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
              <div class="mt-6 space-y-2">
                {% for category, message in messages %}
                  <div class="rounded-lg border px-4 py-3 text-sm mono
                    {% if category == 'error' %} border-rose-400/40 bg-rose-400/10 text-rose-200
                    {% else %} border-emerald-400/40 bg-emerald-400/10 text-emerald-200 {% endif %}">
                    {{ message }}
                  </div>
                {% endfor %}
              </div>
            {% endif %}
          {% endwith %}
        </div>
      </div>
    </div>
  </body>
</html>

