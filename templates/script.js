const navToggleLabel = document.querySelector('.nav-toggle-label');
navToggleLabel.style.position = 'absolute';
navToggleLabel.style.top = '0';
navToggleLabel.style.left = '0';
navToggleLabel.style.marginLeft = '1em';
navToggleLabel.style.height = '100%';
navToggleLabel.style.display = 'flex';
navToggleLabel.style.alignItems = 'center';

const span = navToggleLabel.querySelector('span');
span.style.display = 'block';
span.style.background = 'white';
span.style.height = '2px';
span.style.width = '2em';
span.style.borderRadius = '2px';
span.style.position = 'relative';
  
const beforeSpan = span.cloneNode(true);
const afterSpan = span.cloneNode(true);
span.appendChild(beforeSpan);
span.appendChild(afterSpan);
  
beforeSpan.style.content = "''";
beforeSpan.style.position = 'absolute';
beforeSpan.style.bottom = '7px';
  
afterSpan.style.content = "''";
afterSpan.style.position = 'absolute';
  