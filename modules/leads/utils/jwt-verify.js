import { verifyJWTToken } from '../libs/auth';

const verify_JWT = async(req, res, next) => {

  let token = null;
  if (req.headers && req.headers.authorization) {
    const authorization = req.headers.authorization.split(' ');
    token = authorization[1];
  }
  
  await verifyJWTToken(token)
    .then((decodedToken) => {
      req.user = { ...decodedToken, token }
      next()
    })
    .catch(err => {
      next();
    });
}

export default verify_JWT;