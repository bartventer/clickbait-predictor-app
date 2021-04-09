import React, {useState, useEffect} from 'react';
import Form from './Form';
import Header from './Header';
import Footer from './Footer';
import Outcome from "./Outcome";

function App(){

    const [outcome, setOutcome]=useState([]);

    const [prediction, setPrediction]=useState('');

    const [fetchInProgress, setFetchInProgress]=useState(false);

    useEffect(() => {
        fetch('/api').then(response => {
            if(response.ok){
                return response.json()
            }
        }).then(data => setOutcome(data))
    },[])

    function handleFormChange(inputValue){
        setPrediction(inputValue);
    }

    function handleFormSubmit(){
        setFetchInProgress(true);
        fetch('/api/predict', {
            method: 'POST',
            body: JSON.stringify({
                title:prediction
            }),
            headers: {
                "Content-Type": "application/json; charset=UTF-8"
                }
        }).then(response => response.json())
        .then(message => {
            console.log(message);
            setPrediction('');
            getLatestOutcomes();
            setFetchInProgress(false);
            })
        }

    function getLatestOutcomes(){
        fetch('/api').then(response => {
            if(response.ok){
                return response.json()
            }
        }).then(data => 
           setOutcome(data))
    }

    function deleteOutcome(id){
        setFetchInProgress(true);
        fetch('api/delete', {
            method: 'POST',
            body: JSON.stringify({
                id_num:id
            }),
            headers: {
                "Content-Type": "application/json; charset=UTF-8"
                }
        }).then(response => response.json())
        .then(message => {
            console.log(message);
            getLatestOutcomes();
            setFetchInProgress(false);
            })
        }

    return <div>
            <Header/>
            {/* <h3 className="guidance"></h3> */}
            <Form userInput={prediction} onFormChange={handleFormChange} onFormSubmit={handleFormSubmit} fetchStatus={fetchInProgress}/>
            
            <Outcome
              outcomeList={outcome}
              onDelete={deleteOutcome}
              fetchStatus={fetchInProgress}
            />

          <Footer/>

          </div>
}

export default App;