import LeadService from '../../services/LeadService';

const get_all_leads = async (req, res) => {
  try {

    const { first_name, last_name, email } = req.body;
    if (!first_name || !last_name || !email) {
      return res.status(400).json({ message: 'All params are required.' })
    }

    const addLead = await LeadService.addLead({
      first_name,
      last_name,
      email,
    })

    return res.status(200).json({
      create: true,
      data: addLead
    })

  } catch (err) {
    return res.status(500).json({ message: err.message });
  }
}

export default get_all_leads;