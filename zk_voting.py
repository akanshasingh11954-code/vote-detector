<!doctype html>
<html lang="en" class="h-full bg-black">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Register • Cyber‑Vault Voting</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
      :root { color-scheme: dark; }
      .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }
      .neon { box-shadow: 0 0 0 1px rgba(34,211,238,.35), 0 0 24px rgba(34,211,238,.12); }
    </style>
  </head>
  <body class="h-full text-slate-100">
    <div class="min-h-full bg-gradient-to-b from-black via-slate-950 to-black">
      <div class="mx-auto max-w-xl px-4 py-10">
        <div class="rounded-2xl border border-cyan-400/30 bg-slate-950/80 p-6 neon">
          <div class="mono text-cyan-300 text-xs tracking-widest">QUICK REGISTER</div>
          <h1 class="mt-3 text-2xl font-semibold">Register Aadhaar</h1>
          <p class="mt-2 text-slate-300 text-sm leading-relaxed">
            Type your Aadhaar once. We’ll show only a masked preview and move you straight to voting.
          </p>

          <form method="post" class="mt-6 space-y-4" id="regForm">
            <div>
              <label class="block mono text-xs text-slate-300">Aadhaar (masked input)</label>
              <input
                id="aadhaar_display"
                type="text"
                inputmode="numeric"
                autocomplete="off"
                placeholder="**** **** 1234"
                class="mt-2 w-full rounded-lg border border-cyan-400/30 bg-black/50 px-4 py-3 mono text-cyan-200 outline-none focus:border-cyan-300/70"
              />
              <input type="hidden" name="aadhaar_raw" id="aadhaar_raw" />
              <div class="mt-2 text-xs text-slate-400">
                Hint: digits only; spaces allowed. We keep only the digits you type (locally) and send them once.
              </div>
            </div>

            <div class="flex gap-3">
              <button
                type="submit"
                class="inline-flex items-center justify-center rounded-lg border border-cyan-400/40 bg-cyan-400/10 px-4 py-2 mono text-sm text-cyan-200 hover:bg-cyan-400/15 transition"
              >
                Continue to Vote
              </button>
              <a
                href="/"
                class="inline-flex items-center justify-center rounded-lg border border-slate-700 bg-slate-900/40 px-4 py-2 mono text-sm text-slate-200 hover:bg-slate-900/70 transition"
              >
                Back
              </a>
            </div>
          </form>

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

        {% if aadhaar_preview %}
          <div class="mt-6 rounded-xl border border-cyan-400/20 bg-slate-950/60 p-4">
            <div class="mono text-xs text-cyan-300">REGISTERED PREVIEW</div>
            <div class="mt-2 mono text-sm text-cyan-200">{{ aadhaar_preview }}</div>
            <div class="mt-2 text-sm text-slate-300 leading-relaxed">
              This preview is for UI only. The flat-file ledger remains vote-only aggregates + nullifier set (no vote links).
            </div>
          </div>
        {% endif %}
      </div>
    </div>

    <script>
      // Client-side masking: show **** **** 1234 while keeping digits in a hidden field.
      const display = document.getElementById('aadhaar_display');
      const raw = document.getElementById('aadhaar_raw');

      function normalizeDigits(s) {
        return (s || '').replace(/\D/g, '');
      }

      function formatMasked(digits) {
        const last4 = digits.slice(-4);
        const maskedLen = Math.max(0, digits.length - 4);
        const masked = '*'.repeat(maskedLen);
        const combined = (masked + last4).padStart(4, '*');
        // Group into blocks of 4 for readability.
        return combined.replace(/(.{4})/g, '$1 ').trim();
      }

      display.addEventListener('input', () => {
        const digits = normalizeDigits(display.value);
        raw.value = digits;
        display.value = formatMasked(digits);
      });

      document.getElementById('regForm').addEventListener('submit', () => {
        // Ensure raw digits are sent even if user pasted formatted text.
        raw.value = normalizeDigits(raw.value || display.value);
      });
    </script>
  </body>
</html>

