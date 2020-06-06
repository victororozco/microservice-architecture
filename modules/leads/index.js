// External
import express from 'express';
import bodyParser from 'body-parser';
// Routes
import { LeadsRouter } from './routes';
// Utils
import { JWT_Verify } from './utils';

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const port = process.env.PORT || 8001;

app.use('*', JWT_Verify)

app.use('/api/v1/leads', LeadsRouter);

app.listen(port, () => {
  console.log(`Server is running on PORT ${port}`);
})

export default app;