import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Hidden from '@material-ui/core/Hidden';

const useStyles = makeStyles({
  card: {
    width: "inherit",
    height: "inherit",
  },
  cardDetails: {
    flex: 1,
  },
  cardMedia: {
    height: "auto",
    width: "auto",
    maxHeight: '500px',
    maxWidth: '500px',

  },
  cardActionArea: {
    height: '500px',
    width: '500px',
  },
});

export default function FeaturedPost(props) {
  const classes = useStyles();
  const { post } = props;

  return (
    <Grid item xs={12} md={6}>
      <CardActionArea component="a" className={classes.cardActionArea}>
        <Card className={classes.card}>
          <CardMedia className={classes.cardMedia} image={post.image} title={post.imageTitle} />
          <div className={classes.cardDetails}>
            <CardContent>
              {/*<Typography component="h2" variant="h5">*/}
              {/*  {post.title}*/}
              {/*</Typography>*/}

              {/*<Typography variant="subtitle1" paragraph>*/}
              {/*  {post.image}*/}
              {/*</Typography>*/}
            </CardContent>
          </div>
        </Card>
      </CardActionArea>
    </Grid>
  );
}

FeaturedPost.propTypes = {
  post: PropTypes.object,
};
