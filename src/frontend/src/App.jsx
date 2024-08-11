import './App.css'
import KedroViz from '@quantumblack/kedro-viz'
import '@quantumblack/kedro-viz/lib/styles/styles.min.css'
import data from './main.json'

function App() {

  return (
    <div style={{ height: `100%`, width: `100%` }}>
      <KedroViz
        data={data}
      />
    </div>
  )
}

export default App
