import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import IconButton from '@material-ui/core/IconButton';
import StarBorderIcon from '@material-ui/icons/StarBorder';
import DeleteForeverIcon from '@material-ui/icons/DeleteForever';

/**
 * The data is structured as follows:
 *
 * import image from 'path/to/image.jpg';
 * [etc...]
 *
 * const tileData = [
 *   {
 *     img: image,
 *     title: 'Image',
 *     author: 'author',
 *     featured: true,
 *   },
 *   {
 *     [etc...]
 *   },
 * ];
 */
function AdvancedGridList(props) {

  const useStyles = makeStyles((theme) => ({
    root: {
      display: 'flex',
      flexWrap: 'wrap',
      justifyContent: 'space-around',
      overflow: 'hidden',
      backgroundColor: theme.palette.background.paper,
      backgroundImage: 'url("https://www.transparenttextures.com/patterns/asfalt-dark.png")',
    },
    gridList: {
      width: 500,
      height: 450,
      // Promote the list into his own layer on Chrome. This cost memory but helps keeping high FPS.
      transform: 'translateZ(0)',
    },
    titleBar: {
      background:
        'linear-gradient(to bottom, rgba(0,0,0,0.7) 0%, ' +
        'rgba(0,0,0,0.3) 70%, rgba(0,0,0,0) 100%)',
    },
    icon: {
      color: 'white',
    },
  }));

  const classes = useStyles();

  const defualtItems = ["“How to Achieve Results Using This One Weird Trick”","“You'll Never Believe This _________ “","“They Didn't Know _________ . Then This Happened …”"];
  
  const featuredItems = [0,3,9,11,17];

  function handleDelete(event){
    props.onDelete(event.target.value)
  }

  return (
    <div className={classes.root}>
      <GridList cellHeight={200} spacing={1} className={classes.gridList}>
        {props.outcomeList.map((outcomeItem, index) => (
          <GridListTile key={index} cols={featuredItems.includes(index) ? 2 : 1} rows={featuredItems.includes(index) ? 2 : 1}>
            <img src={outcomeItem.imgUrl} alt={outcomeItem.result} />
            <GridListTileBar
              title={outcomeItem.prediction}
              titlePosition="top"
              actionIcon={
                <IconButton aria-label={`star ${outcomeItem.prediction}`} className={classes.icon}>
                  { defualtItems.includes(outcomeItem.prediction)? <StarBorderIcon value={index}/>:<DeleteForeverIcon onClick={handleDelete} value={index}/>}
                </IconButton>
              }
              actionPosition="left"
              className={classes.titleBar}
            />
          </GridListTile>
        ))}
      </GridList>
    </div>
  );
}

export default AdvancedGridList;