import jwt from 'jsonwebtoken';
const JWT_SECRET = process.env.JWT_SECRET;

export function verifyJWTToken(token) {
  return new Promise((resolve, reject) => {
    jwt.verify(token, JWT_SECRET, (err, decodedToken) => {
      if (err || !decodedToken) {
        return reject(err);
      }

      resolve(decodedToken);
    })
  })
}