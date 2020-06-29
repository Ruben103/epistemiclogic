import React from 'react';

import { makeStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import GitHubIcon from '@material-ui/icons/GitHub';
import FacebookIcon from '@material-ui/icons/Facebook';
import TwitterIcon from '@material-ui/icons/Twitter';
import Header from './Header';
import MainFeaturedPost from './MainFeaturedPost';
import FeaturedPost from './FeaturedPost';
import Main from './Main';
import Sidebar from './Sidebar';
import Footer from './Footer';
import post1 from './blog-post.1.md';
import post2 from './blog-post.2.md';
import post3 from './blog-post.3.md';
import introArticle from './introArticle.md';
import strategiesArticle from './strategiesArticle.md';

const useStyles = makeStyles((theme) => ({
  mainGrid: {
    marginTop: theme.spacing(3),
  },
}));

const sections = [
  { title: 'Introduction', url: '#intro' },
  { title: 'Theoretical Justification', url: '#theory' },
  { title: 'Strategies', url: '#' },
  { title: 'Experiments', url: '#' },
  { title: 'Discussion', url: '#' },
  { title: 'Conclusion', url: '#' },
];

const mainFeaturedPost = {
  title: 'An epistemic approach to Liar\'s Dice',
  description:
    "",
  image: 'https://source.unsplash.com/random',
  imgText: 'main image description',
  // linkText: 'Continue reading…',
};

const featuredPosts = [
  {
    title: 'Example 1',
    description:
      'There are four players in the game, each holding three dice.The  distribution  is  as  follows: D={(1,2,2),(1,1,3),(3,5,6),(4,3,6)}.   The starting player of the round opens his bidding and says”Two two’s”.  The next player has two choices: raise the value or the quantity. The player chooses to say ”Three two’s”, which means he has overbid the quantity.\n',
    image: 'https://source.unsplash.com/random',
    imageText: 'Image Text',
  },
  {
    title: 'Example 2',
    description:
      'Marie has just made the bidding ”Two sixes”. John is the only allowed to increase the quantity, because no eyes are higher than six.  Johnis then allowed to say ”Three three’s,  he does not have to say ”Three Sixes”. When the quantity is increased, the value may be ’reset’.  NOTE: John is also allowed to skip quantities: he could have immediately went from three to seven.\n',
    image: 'https://source.unsplash.com/random',
    imageText: 'Image Text',
  },
];

const posts = [post1, post2, post3];



export default function Blog() {
  const classes = useStyles();

  return (

    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="lg">
        <Header title="Liar's Dice" sections={sections} />
        <main>
          <MainFeaturedPost post={mainFeaturedPost} />
          {/*<Grid container spacing={5} className={classes.mainGrid}>*/}
            <Main title="" posts={[introArticle]} />
            <Grid container spacing={2} direction="row"
                  alignItems="center"
                  justify="center"
                  >
              {featuredPosts.map((post) => (
                  <FeaturedPost key={post.title} post={post} />
              ))}
            </Grid>
            <Main title="" posts={[strategiesArticle]} />
            <iframe src="./src/blog/LAMAS_paper.pdf" width="100%" height="1080px"/>

          {/*<Sidebar*/}
            {/*  title={sidebar.title}*/}
            {/*  description={sidebar.description}*/}
            {/*  archives={sidebar.archives}*/}
            {/*  social={sidebar.social}*/}
            {/*/>*/}
          {/*</Grid>*/}
        </main>
      </Container>
      {/*<Footer title="Footer" description="Something here to give the footer a purpose!" />*/}
    </React.Fragment>
  );
}
