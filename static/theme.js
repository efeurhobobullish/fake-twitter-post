document.addEventListener('DOMContentLoaded', () => {
  const themeToggleBtn = document.getElementById('theme-toggle')
  const htmlEl = document.documentElement

  // Load saved theme or default to light
  const savedTheme = localStorage.getItem('theme') || 'light'
  if (savedTheme === 'dark') {
    htmlEl.classList.add('dark')
    htmlEl.setAttribute('data-theme', 'dark')
  } else {
    htmlEl.classList.remove('dark')
    htmlEl.setAttribute('data-theme', 'light')
  }

  themeToggleBtn.addEventListener('click', () => {
    if (htmlEl.classList.contains('dark')) {
      htmlEl.classList.remove('dark')
      htmlEl.setAttribute('data-theme', 'light')
      localStorage.setItem('theme', 'light')
    } else {
      htmlEl.classList.add('dark')
      htmlEl.setAttribute('data-theme', 'dark')
      localStorage.setItem('theme', 'dark')
    }
  })
})
