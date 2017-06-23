from django.forms import ValidationError

from edc_base.modelform_validators import FormValidator
from edc_constants.constants import NO


class BloodResultFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            NO,
            field='are_results_normal',
            field_required='abnormal_results_in_ae_range')

        creatinine_field = 'creatinine'
        creatinine_unit = self.cleaned_data.get('creatinine_unit')

        self.validate_non_decimal_values(field=creatinine_field,
                                         field_unit=creatinine_unit)

        magnesium_field = 'magnesium'
        magnesium_unit = self.cleaned_data.get('magnesium_unit')

        self.validate_non_decimal_values(field=magnesium_field,
                                         field_unit=magnesium_unit)

        urea_field = 'urea'
        urea_unit = self.cleaned_data.get('urea_unit')

        self.validate_non_decimal_values(field=urea_field,
                                         field_unit=urea_unit)

        return self.cleaned_data

    def validate_non_decimal_values(self, field=None, field_unit=None):
        if ((field_unit == 'umol/L' or field_unit == 'mmol/L')
                and len(str(self.cleaned_data.get(field)).split('.')) == 2):
            raise ValidationError({
                field: 'Please provide a whole number for mmol/L or μmol/L units'})
