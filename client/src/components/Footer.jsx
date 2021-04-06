  import React from "react";
  import LinkedInIcon from '@material-ui/icons/LinkedIn';
  import GitHubIcon from '@material-ui/icons/GitHub';
  import FacebookIcon from '@material-ui/icons/Facebook';
  import Typography from '@material-ui/core/Typography';
  import Link from '@material-ui/core/Link';

function Footer() {
  const year = new Date().getFullYear();
  return (
    <footer>
      <p>Copyright ⓒ Bart Venter {year}</p>
      <Typography >
      <Link href={"https://www.linkedin.com/in/bart-venter-ca-sa-606bb0141/"}>
      <LinkedInIcon className="footerbutton"/>
      </Link>
      <Link href={"https://github.com/bartventer?tab=repositories"}>
      <GitHubIcon className="footerbutton"/>
      </Link>
      <Link href={"https://www.facebook.com/bart.venter.12"}>
      <FacebookIcon className="footerbutton"/>
      </Link>
      </Typography>
    </footer>
  );
}

export default Footer;