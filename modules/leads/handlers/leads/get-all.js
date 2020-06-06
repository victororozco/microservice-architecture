import LeadService from '../../services/LeadService';

const get_all_leads = async (req, res) => {
  try {
    const allLeads = await LeadService.getAllLeads();

    return res.status(200).json({
      data: allLeads,
    })

  } catch (err) {
    return res.status(500).json({ message: err.message });
  }
}

export default get_all_leads;