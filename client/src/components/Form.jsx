import React from 'react';
import RadioButtonCheckedIcon from '@material-ui/icons/RadioButtonChecked';

function Form(props){

    function handleChange(event){
        props.onFormChange(event.target.value)
    }

    function handleSubmit(event){
        event.preventDefault();
        props.onFormSubmit();

    }

    return <form onSubmit={handleSubmit}>
            <input type="text-area" placeholder="Enter the article name here" required minLength="6" value={props.userInput}onChange={handleChange}></input>
            <button type="submit">
                <RadioButtonCheckedIcon/>
            </button>
    </form>
}

export default Form;