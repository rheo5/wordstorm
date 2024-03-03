import { useState, FormEvent } from 'react'; // Import FormEvent
import './App.css';

function App() {
  const [inputWord, setInputWord] = useState<string>(''); // Set type for inputWord
  const [inputSource, setInputSource] = useState<string>('');
  const [similarWords, setSimilarWords] = useState<string[]>([]);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/api/similar-words', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ word: inputWord, source: inputSource })
      });
      if (!response.ok) {
        throw new Error('Failed to fetch');
      }
      const data = await response.json();
      setSimilarWords(data.similarWords);
    } catch (error: any) {
      console.error('Error fetching data:', error.message);
    }
  };  

  return (
    <div className="w-full h-screen flex justify-center items-center">
      <div className="">
        <form onSubmit={handleSubmit} className="text-center flex flex-col gap-3 w-64">
          <input 
            type="text" 
            value={inputSource}
            onChange={(e) => setInputSource(e.target.value)}
            className="form-input text-center" 
            placeholder="Brainstorm context source link" 
          />
          <input 
            type="text" 
            value={inputWord}
            onChange={(e) => setInputWord(e.target.value)}
            className="form-input text-center" 
            placeholder="Brainstorm key word" 
          />
          <div className="flex justify-center">
            <input type="submit" value="Wordstorm!" className="bg-gray-200 rounded-md py-2 hover:bg-gray-300 cursor-pointer w-1/2" />
          </div>
        </form>
        <div>
          {similarWords.map((word, index) => (
            <div key={index}>{word}</div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
