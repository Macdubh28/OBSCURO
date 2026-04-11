const CACHE = 'obscuro-v1';
const ASSETS = [
  '/OBSCURO/',
  '/OBSCURO/index.html',
  '/OBSCURO/protocoles.html',
  '/OBSCURO/citations.html',
  '/OBSCURO/journal.html',
  '/OBSCURO/manifest.json'
];
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(ASSETS))
  );
});
self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request))
  );
});
