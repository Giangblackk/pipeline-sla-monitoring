import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import KedroViz from '@quantumblack/kedro-viz'
import '@quantumblack/kedro-viz/lib/styles/styles.min.css'
import data from './main.json'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div style={{ height: `100%`, width: `100%`}}>
      <KedroViz
        data={data}
      />
    </div>
  )
}

export default App
