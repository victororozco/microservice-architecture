import express from 'express';
// Handlers
import {
  GetAllLeads,
  AddLead,
} from '../handlers/leads';
// Roles
import { LEAD, ALL, ADMIN } from '../utils/roles';

const router = express.Router();
const AUTH = "../utils/auth";

// GET
router.get(
  '/',
  require(AUTH)([ADMIN, LEAD], 'Get all leads'),
  GetAllLeads,
);
// POST
router.post(
  '/',
  require(AUTH)([ALL], 'New lead'),
  AddLead,
);

export default router;