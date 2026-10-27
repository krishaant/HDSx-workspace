# M1 Link Note

My M1 dataset (BC MSP fee-for-service services, patient counts, and
expenditures by gender, specialty, and fiscal year, 2005/06-2009/10; see
`data-intake-card.md`) is counts and dollar totals, not individual claims, so
any plot by specialty × gender risks the same two problems audited here:
truncated axes that exaggerate small differences in spending or patient
counts between genders, and captions that drop the fee-for-service-only
scope. Because the patient-counting rule is undocumented, I also need to
state in every caption that counts cannot be summed across specialties/years
to get a population total, the same way this figure states its own
exclusions and unweighted limitation instead of letting the plot overclaim.
Any specialty × gender cell with very few practitioners or patients needs to
be aggregated or suppressed rather than plotted individually, to avoid the
privacy risk noted in the intake card.
