import React, {useState, useEffect} from 'react';
import Form from './Form';
import Header from './Header';
import Footer from './Footer';
import AdvancedGridList from "./AdvancedGridList";
import { usePromiseTracker } from "react-promise-tracker";

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

    const { promiseInProgress } = usePromiseTracker();

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
            setInProgress(false);
            console.log(message);
            setPrediction('');
            getLatestOutcomes();
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
            setFetchInProgress(false);
            console.log(message);
            getLatestOutcomes();
            })
        }

    return <div>
            <Header/>
            {/* <h3 className="guidance"></h3> */}
            <Form userInput={prediction} onFormChange={handleFormChange} onFormSubmit={handleFormSubmit} fetchStatus={fetchInProgress}/>
            
            <AdvancedGridList
              outcomeList={outcome}
              onDelete={deleteOutcome}
            />

          <Footer/>

          </div>
}

export default App;