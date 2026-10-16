const canvas = document.getElementById('partyCanvas');
const ctx = canvas.getContext('2d');
const greeting = document.getElementById('greeting');
const startButton = document.getElementById('startButton');
const music = document.getElementById('birthdayMusic');
const noteSection = document.getElementById('noteSection');
const noteText = document.getElementById('noteText');
const continueButton = document.getElementById('continueButton');
const ending = document.getElementById('ending');

const confetti = Array.from({length: 95}, () => ({
  x: Math.random() * canvas.width,
  y: Math.random() * canvas.height,
  speed: 0.7 + Math.random() * 1.7,
  size: 2 + Math.random() * 4,
  color: ['#FF69B4','#FFD700','#7DF9FF','#98FB98','#DDA0DD','#FFFFFF'][Math.floor(Math.random()*6)]
}));
let running = false;
let started = false;
let frame = 0;

function roundedRect(x, y, w, h, r, fill) {
  ctx.fillStyle = fill;
  ctx.beginPath();
  ctx.roundRect(x, y, w, h, r);
  ctx.fill();
}
function drawHeart(x,y,size,color) {
  ctx.save(); ctx.translate(x,y); ctx.scale(size/18,size/18);
  ctx.strokeStyle=color; ctx.lineWidth=2; ctx.beginPath();
  ctx.moveTo(0,7); ctx.bezierCurveTo(-22,-7,-10,-20,0,-9);
  ctx.bezierCurveTo(10,-20,22,-7,0,7); ctx.stroke(); ctx.restore();
}
function drawStar(x,y,r,color) {
  ctx.save(); ctx.translate(x,y); ctx.strokeStyle=color; ctx.lineWidth=2;
  ctx.beginPath();
  for(let i=0;i<10;i++){ const a=-Math.PI/2+i*Math.PI/5; const rr=i%2?r*.45:r;
    const px=Math.cos(a)*rr, py=Math.sin(a)*rr; i===0?ctx.moveTo(px,py):ctx.lineTo(px,py); }
  ctx.closePath(); ctx.stroke(); ctx.restore();
}
function drawFlower(x,y,color) {
  ctx.fillStyle=color;
  for(let i=0;i<5;i++){const a=i*Math.PI*2/5;ctx.beginPath();ctx.arc(x+Math.cos(a)*8,y+Math.sin(a)*8,5,0,Math.PI*2);ctx.fill();}
  ctx.fillStyle='#FFD966';ctx.beginPath();ctx.arc(x,y,4,0,Math.PI*2);ctx.fill();
}
function drawCake() {
  // plate
  ctx.fillStyle='#C7D4E8'; ctx.beginPath(); ctx.ellipse(300,325,142,27,0,0,Math.PI*2); ctx.fill();
  ctx.fillStyle='#F4F4F4'; ctx.beginPath(); ctx.ellipse(300,320,132,23,0,0,Math.PI*2); ctx.fill();
  // lower and upper layers
  roundedRect(170,245,260,72,8,'#B56A4B');
  roundedRect(170,245,260,15,5,'#FFF0D9');
  roundedRect(200,185,200,62,8,'#F3A6C8');
  roundedRect(200,185,200,13,5,'#FFF0D9');
  for(const x of [220,260,300,340,380]) { ctx.fillStyle='#FFF0D9';ctx.beginPath();ctx.arc(x,197,8,0,Math.PI*2);ctx.fill(); }
  for(const x of [225,265,305,345,375]) { ctx.fillStyle='#FFFFFF';ctx.beginPath();ctx.arc(x,220,5,0,Math.PI*2);ctx.fill(); }
  const candleColors=['#FFD700','#7DF9FF','#FF69B4','#98FB98'];
  for(let i=0;i<4;i++){
    const x=240+i*40;
    roundedRect(x-5,145,10,42,3,candleColors[i]);
    ctx.strokeStyle='#FFFFFF';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x-3,165);ctx.lineTo(x+3,172);ctx.stroke();
    const flame=8+Math.random()*5;
    ctx.fillStyle=['#FFD700','#FFA500','#FFFF99'][Math.floor(Math.random()*3)];
    ctx.beginPath();ctx.ellipse(x,137,flame*.65,flame,0,0,Math.PI*2);ctx.fill();
    ctx.fillStyle='#FFFFFF';ctx.beginPath();ctx.arc(x,138,3,0,Math.PI*2);ctx.fill();
  }
}
function draw() {
  ctx.clearRect(0,0,canvas.width,canvas.height);
  // subtle background
  ctx.fillStyle='rgba(255,255,255,.24)';ctx.fillRect(0,0,canvas.width,canvas.height);
  // corner doodles
  drawHeart(55,42,18,'#F4A6C8'); drawStar(92,35,14,'#75BDEB'); drawFlower(52,82,'#F6B8D0');
  drawHeart(545,42,18,'#F4A6C8'); drawStar(508,35,14,'#75BDEB'); drawFlower(548,82,'#F6B8D0');
  drawHeart(55,385,18,'#F4A6C8'); drawStar(92,390,14,'#75BDEB'); drawFlower(52,345,'#F6B8D0');
  drawHeart(545,385,18,'#F4A6C8'); drawStar(508,390,14,'#75BDEB'); drawFlower(548,345,'#F6B8D0');
  // confetti
  for(const p of confetti){
    p.y += p.speed;
    if(p.y>canvas.height){p.y=-5;p.x=Math.random()*canvas.width;}
    ctx.fillStyle=p.color;ctx.beginPath();ctx.arc(p.x,p.y,p.size,0,Math.PI*2);ctx.fill();
  }
  drawCake();
  if(running) frame++;
  requestAnimationFrame(draw);
}
draw();

const note = `Happiest Birthday to my dearest Auntyjiiii,
my Lady Boss, and a teacher who will always
occupy a very special place in my heart.

Some people leave an impression on us through
extraordinary gestures, while others become
unforgettable through the smallest moments.
You, Ma'am, have somehow managed to do both.
And perhaps the most beautiful thing about
knowing you is that you may never fully realise
how profoundly your kindness has touched
the heart of your student.

I still treasure those little names you gave me:
PA, bunu, your real treasure.
To you, they might have been simple words,
spoken in passing. To me, they became little
keepsakes of a chapter in my life I will always
look back upon with fondness.

You taught me lessons beyond textbooks, gave
me encouragement when I needed it, and created
memories whose significance has only grown
with time.

And now, a formal complaint from your
neglected PA. Madam, the gossip department
is overflowing! I have accumulated enough
tea for an entire documentary, yet its most
distinguished listener remains perpetually
occupied. Should I submit my reports in writing?
Appoint the walls as temporary management?
Please advise.

Jokes aside, sometimes something happens and
my immediate instinct is to share it with you.
Then reality reminds me that life has become
busier, and I quietly save the story for another
day.

I understand, Ma'am, that responsibilities grow
and circumstances change. Still, it is possible
to understand someone's absence and miss their
presence at the same time. And I suppose that
is what happens when ordinary conversations
become cherished parts of one's day.

As you begin another year of life, I hope
happiness finds you in the quietest corners,
peace accompanies you through every uncertainty,
and love surrounds you in ways that make you
feel truly cherished.

May this new chapter be as beautiful as the
kindness you have given to others.

Perhaps years from now, when these school days
have become distant memories, I will still
remember you with the same gratitude: the
teacher who made a difference without perhaps
ever knowing the full extent of it.

Happy Birthday, Auntyjiiii.

Thank you for being a memorable part of my story.
May life always be generous to you, and may
your beautiful smile never lose its light.

With immense respect, endless gratitude,
a tiny unresolved complaint, and approximately
seventeen pending gossip reports,

Your PA, forever grateful to have been your student.`;


function addNoteParagraphs() {
  noteText.innerHTML = '';

  note.split(/\n\s*\n/).forEach(part => {
    const p = document.createElement('p');
    p.textContent = part.trim();
    noteText.appendChild(p);
  });

  // Restart the scrolling animation
  noteText.classList.remove('scrolling-note');
  void noteText.offsetWidth;
  noteText.classList.add('scrolling-note');
}

startButton.addEventListener('click', async () => {
  if(started) return;
  started = true;
  running = true;
  startButton.textContent = 'Your surprise is playing 💗';
  startButton.disabled = true;
  try { await music.play(); } catch(e) {
    startButton.textContent = 'Surprise started! Tap play on your browser if music is blocked.';
  }
  const message = 'Happy Birthday Auntyjiii !!!!!!!!!!';
  let i = 0;
  const type = () => {
    greeting.textContent = message.slice(0,i++);
    if(i <= message.length) setTimeout(type, 130);
    else setTimeout(() => {
      addNoteParagraphs();
      noteSection.classList.remove('hidden');
      noteSection.scrollIntoView({behavior:'smooth', block:'start'});
    }, 1800);
  };
  type();
});
continueButton.addEventListener('click', () => {
  ending.classList.remove('hidden');
  ending.scrollIntoView({behavior:'smooth', block:'start'});
});
