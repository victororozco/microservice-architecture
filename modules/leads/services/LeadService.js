import db from '../models';

class LeadService {
  static async getAllLeads () {
    try {
      return await db.Leads.findAll();
    } catch (err) {
      return new Error(err);
    }
  }

  static async addLead(newLead) {
    return new Promise(async(resolve, reject) => {
      try {
        const new_lead = await db.Leads.create(newLead);
        return resolve(new_lead);
      } catch (err) {
        return reject(err);
      }
    })
  }
}

export default LeadService;