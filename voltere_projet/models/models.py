from odoo import models, fields, api, exceptions

class VoltereProjet(models.Model):
    _inherit = 'project.task'
    _description = 'Checklist dans taches projet'



    coordonne = fields.Boolean('Coordonnées complètes du client (Nom, prénom, adresse, N° de téléphone)', default=False)
    dln = fields.Boolean('Date et lieu de naissance', default=False)
    autocons = fields.Boolean('Autoconsommation avec ou sans revente de surplus', default=False)
    puissance = fields.Boolean('La puissance du kit installé en Kwc', default=False)
    microo = fields.Boolean('Le nombre de micro-onduleurs', default=False)
    monotri = fields.Boolean('Monophasé ou triphasé', default=False)
    marquemod = fields.Boolean('Marque et modèles du kit photovoltaïque', default=False)
    dp1 = fields.Boolean('DP1 Plan de situation du terrain (cadastre)', default=False)
    dp4 = fields.Boolean('DP4 Un plan des toitures « avant » et « après » travaux (calepinage)', default=False)
    dp7 = fields.Boolean('DP7 Une photo en couleur permettant de situer le terrain dans l’environnement proche', default=False)
    dp8 = fields.Boolean('DP8 Une photo en couleur permettant de situer le terrain dans le paysage lointain',
                         default=False)
    mandat = fields.Boolean('Le mandat signé par votre client pour la partie administrative auprès de la mairie',
                         default=False)
    nombre_modules = fields.Boolean('Le nombre de modules photovoltaïques', default=False)
    nombre_chaines = fields.Boolean('Le nombre de chaînes', default=False)
    nombre_groupes = fields.Boolean('Le nombre de groupes', default=False)
    nombre_onduleurs_protections = fields.Boolean(
        'Le nombre d’onduleurs et de protections contre les surintensités côté DC si elles existent', default=False)
    autres_sources = fields.Boolean('Les autres sources DC ou AC (lorsqu’elles existent)', default=False)
    distribution_dc = fields.Boolean('La distribution DC (s’il y a lieu)', default=False)

    facture_electricite = fields.Boolean(
        'Facture d’électricité mentionnant le N° PDL (Point De Livraison ou PDS ou PCE)', default=False)
    mandat_raccordement = fields.Boolean('Le mandat signé par votre client pour la partie demande de raccordement',
                                         default=False)
    taxe_fonciere = fields.Boolean('La taxe foncière (preuve de propriété)', default=False)
    plan_masse = fields.Boolean('Un plan de masse mentionnant', default=False)
    nombre_panneaux = fields.Boolean('Le nombres de panneaux photovoltaïques', default=False)
    compteur_disjoncteur = fields.Boolean('Le compteur / disjoncteur de consommation', default=False)
    coffret_viabilisation = fields.Boolean('Le coffret de viabilisation (généralement à l’extérieur)', default=False)
    photo_tableau_electrique = fields.Boolean('Photo en couleur du tableau électrique', default=False)
    photo_compteur_disjoncteur = fields.Boolean('Photo en couleur du compteur et disjoncteur (LINKY)', default=False)
    date_raccordement_souhaitee = fields.Boolean('Date souhaitée de raccordement', default=False)

    stage_ok = fields.Boolean('Stage OK', compute='_compute_stage_ok', store=True)

    @api.depends('coordonne', 'dln', 'autocons', 'puissance', 'microo', 'monotri',
                 'marquemod', 'dp1', 'dp4', 'dp7', 'dp8', 'mandat', 'nombre_modules',
                 'nombre_chaines', 'nombre_groupes', 'nombre_onduleurs_protections',
                 'autres_sources', 'distribution_dc', 'facture_electricite', 'mandat_raccordement',
                 'taxe_fonciere', 'plan_masse', 'nombre_panneaux', 'compteur_disjoncteur',
                 'coffret_viabilisation', 'photo_tableau_electrique', 'photo_compteur_disjoncteur',
                 'date_raccordement_souhaitee')
    def _compute_stage_ok(self):
        for record in self:
            checklist_fields = [
                record.coordonne, record.dln, record.autocons, record.puissance,
                record.microo, record.monotri, record.marquemod, record.dp1,
                record.dp4, record.dp7, record.dp8, record.mandat, record.nombre_modules,
                record.nombre_chaines, record.nombre_groupes, record.nombre_onduleurs_protections,
                record.autres_sources, record.distribution_dc, record.facture_electricite,
                record.mandat_raccordement, record.taxe_fonciere, record.plan_masse,
                record.nombre_panneaux, record.compteur_disjoncteur, record.coffret_viabilisation,
                record.photo_tableau_electrique, record.photo_compteur_disjoncteur,
                record.date_raccordement_souhaitee
            ]

            # Set stage_ok to True if at least one field is True
            record.stage_ok = any(checklist_fields)

    @api.model
    def create(self, vals):
        # Your create method logic here
        return super(VoltereProjet, self).create(vals)

    def write(self, vals):
        if 'stage_id' in vals and not self.stage_ok:
            raise exceptions.UserError("Please check 'dln' before changing the 'stage_id'.")

        # Your write method logic here
        return super(VoltereProjet, self).write(vals)







