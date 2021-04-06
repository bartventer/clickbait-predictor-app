import React, {useState, useEffect} from 'react';
import Form from './Form';
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import IconButton from '@material-ui/core/IconButton';
import DeleteForeverIcon from '@material-ui/icons/DeleteForever';
import Header from './Header';
import Footer from './Footer';

function App(){

    const [outcome, setOutcome]=useState([]);

    const [prediction, setPrediction]=useState('');

    useEffect(() => {
        fetch('/api').then(response => {
            if(response.ok){
                return response.json()
            }
        }).then(data => setOutcome(data))
    },[])

    function handleFormChange(inputValue){
        setPrediction(inputValue)
    }

    function handleFormSubmit(){
        fetch('api/predict', {
            method: 'POST',
            body: JSON.stringify({
                title:prediction
            }),
            headers: {
                "Content-Type": "application/json; charset=UTF-8"
                }
        }).then(response => response.json())
        .then(message => {
            console.log(message)
            setPrediction('')
            getLatestOutcomes()
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
            console.log(message)
            getLatestOutcomes()
            })
        }


    const useStyles = makeStyles((theme) => ({
        root: {
          display: 'flex',
          flexWrap: 'wrap',
          justifyContent: 'space-around',
          overflow: 'hidden',
          backgroundImage: 'url("https://www.transparenttextures.com/patterns/asfalt-dark.png")',
          marginTop: "70px"
        },
        gridList: {
          flexWrap: 'nowrap',
          transform: 'translateZ(0)',
        
        },
        title: {
          color: theme.palette.primary.light,
        },
        titleBar: {
          background:
            'linear-gradient(to top, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.3) 70%, rgba(0,0,0,0) 100%)',
        }
      }));

      const classes = useStyles();

    return <div>
            <Header/>
            <h3 className="guidance">There's too much clickbait going around. Simply enter the name of the article and the site will predict whether the piece is clickbait or not. We'll generate an image with your result.</h3>
            <Form userInput={prediction} onFormChange={handleFormChange} onFormSubmit={handleFormSubmit}/>
            
            <div className={classes.root}>
            <GridList className={classes.gridList} cols={2.5} cellHeight={250}>
            {outcome.map((outcomeItem, index) => (
            <GridListTile key={index}>
            <img src={outcomeItem.imgUrl} alt={outcomeItem.result} />
            <GridListTileBar
              title={outcomeItem.result}
              subtitle={outcomeItem.prediction}
              titlePosition={'bottom'}
              classes={{
                root: classes.titleBar,
                title: classes.title,
              }}
              actionIcon={
                <IconButton aria-label={`star ${outcomeItem.prediction}`} onClick={()=> deleteOutcome(index)}>
                  <DeleteForeverIcon className={classes.title} />
                </IconButton>
              }
            />
            </GridListTile>
        ))}
      </GridList>
    </div>

    <Footer/>

    </div>
}

export default App;