import fs from 'fs';
const s = fs.readFileSync(process.argv[2] || 'index.html', 'utf8');
const blocks = [...s.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
let bad = 0;
blocks.forEach((b, i) => { try { new Function(b); } catch (e) { bad++; console.log('BAD block', i, e.message.slice(0, 80)); } });
console.log('blocks:', blocks.length, 'bad:', bad);
