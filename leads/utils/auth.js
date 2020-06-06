import { ALL } from './roles';

module.exports = (roles, action = '') => {
  return (req, res, next) => {
    const data = req.body;
    console.info('request: ', action, req.baseUrl, req.method, JSON.stringify(data));
    if (req.user) {
      if (roles.includes(req.user.role) || roles.includes(ALL))
        next();
      else
        return res.status(403).json({
          message: "[AUTH001] Debe inciar sesión o registrarse para ejecutar esta acción."
        });

      /* without token and is public access */
    } else if (!req.user && roles.includes(ALL)) {
      next();
      /* Save logs without token and is not public access */
    } else {
      return res.status(403).json({
        message: "[AUTH002] Debe inciar sesión o registrarse para ejecutar esta acción."
      });
    }
  }
}