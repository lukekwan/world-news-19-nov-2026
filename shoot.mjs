// Renders poster.html to entry.png (exactly 1024x1024) with headless Chromium.
//
// Needs a Playwright driver available to Node. It is loaded through
// createRequire so the script works wherever the driver lives:
//   - default: resolves 'playwright-core' next to this script, or
//   - set PLAYWRIGHT_REQUIRE_FROM to a file inside a directory that has
//     playwright-core installed (e.g. /tmp/pw-render/package.json).
// The browser binary is found via Playwright's own cache; override it with
// CHROMIUM_PATH if needed.
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const require = createRequire(process.env.PLAYWRIGHT_REQUIRE_FROM || import.meta.url);
const { chromium } = require('playwright-core');

const dir = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(dir, 'poster.html');
const outPath = path.join(dir, 'entry.png');

const browser = await chromium.launch({
  executablePath: process.env.CHROMIUM_PATH || undefined,
  args: ['--no-sandbox', '--disable-dev-shm-usage', '--force-device-scale-factor=1'],
});
const page = await browser.newPage({ viewport: { width: 1024, height: 1024 }, deviceScaleFactor: 1 });
await page.goto('file://' + htmlPath, { waitUntil: 'load' });
await page.waitForTimeout(300);
await page.screenshot({ path: outPath });
await browser.close();
console.log('wrote', outPath);
