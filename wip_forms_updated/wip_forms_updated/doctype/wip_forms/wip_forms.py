# Copyright (c) 2024, Dharmaraj and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class WIPForms(Document):
# 	pass

import frappe
from frappe.model.document import Document
from frappe import _

class WIPForms(Document):
    def validate(self):
        self.deal_name = self.client_name + ' ' +self.property_location
        errors = []

        if self.mobile:
            mobile_error = self.validate_mobile()
            if mobile_error:
                errors.append(mobile_error)
        
        if self.email:
            email_error = self.validate_email()
            if email_error:
                errors.append(email_error)

        if errors:
            frappe.throw("\n".join(errors))

    def validate_mobile(self):
        if not self.mobile.startswith("+91-") or not self.mobile[4:].isdigit() or len(self.mobile[4:]) != 10:
            return _("Mobile number must start with '+91-' followed by a 10-digit numeric value")
        return None

    def validate_email(self):
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, self.email):
            return _("Invalid email format")
        return None

    # def before_save(self):
    #     if self.deal_type == 'Outright/Sale' and self.area and self.rate and self.area_unit and self.rate_unit:
    #         if self.area_unit == 'Square Meter':
    #             if self.rate_unit == "Square Centimeter":
    #                 self.conversion_factor_between_area_and_rate = 0.0001
    #             elif self.rate_unit == "Square Foot":
    #                 self.conversion_factor_between_area_and_rate = 0.09290304
    #             elif self.rate_unit == "Square Inch":
    #                 self.conversion_factor_between_area_and_rate = 0.00064516
    #             elif self.rate_unit == "Square Kilometer":
    #                 self.conversion_factor_between_area_and_rate = 1000000
    #             elif self.rate_unit == "Square Meter":
    #                 self.conversion_factor_between_area_and_rate = 1
    #             elif self.rate_unit == "Square Mile":
    #                 self.conversion_factor_between_area_and_rate = 2589988.11
    #             elif self.rate_unit == "Square Yard":
    #                 self.conversion_factor_between_area_and_rate = 0.83612736

    #         elif self.area_unit == 'Square Centimeter':
    #             if self.rate_unit == "Square Centimeter":
    #                 self.conversion_factor_between_area_and_rate = 1
    #             elif self.rate_unit == "Square Foot":
    #                 self.conversion_factor_between_area_and_rate = 929.0304
    #             elif self.rate_unit == "Square Inch":
    #                 self.conversion_factor_between_area_and_rate = 645.16
    #             elif self.rate_unit == "Square Kilometer":
    #                 self.conversion_factor_between_area_and_rate = 10000000000
    #             elif self.rate_unit == "Square Meter":
    #                 self.conversion_factor_between_area_and_rate = 10000
    #             elif self.rate_unit == "Square Mile":
    #                 self.conversion_factor_between_area_and_rate = 2.59e+10

    #         elif self.area_unit == 'Square Foot':
    #             if self.rate_unit == "Square Centimeter":
    #                 self.conversion_factor_between_area_and_rate = 1.07639104e-5
    #             elif self.rate_unit == "Square Foot":
    #                 self.conversion_factor_between_area_and_rate = 1
    #             elif self.rate_unit == "Square Inch":
    #                 self.conversion_factor_between_area_and_rate = 0.00694444
    #             elif self.rate_unit == "Square Kilometer":
    #                 self.conversion_factor_between_area_and_rate = 92903.04
    #             elif self.rate_unit == "Square Meter":
    #                 self.conversion_factor_between_area_and_rate = 0.09290304
    #             elif self.rate_unit == "Square Mile":
    #                 self.conversion_factor_between_area_and_rate = 27878400
    #             elif self.rate_unit == "Square Yard":
    #                 self.conversion_factor_between_area_and_rate = 9

    #         elif self.area_unit == 'Square Inch':
    #             if self.rate_unit == "Square Centimeter":
    #                 self.conversion_factor_between_area_and_rate = 0.00064516
    #             elif self.rate_unit == "Square Foot":
    #                 self.conversion_factor_between_area_and_rate = 144
    #             elif self.rate_unit == "Square Inch":
    #                 self.conversion_factor_between_area_and_rate = 1
    #             elif self.rate_unit == "Square Kilometer":
    #                 self.conversion_factor_between_area_and_rate = 6451600
    #             elif self.rate_unit == "Square Meter":
    #                 self.conversion_factor_between_area_and_rate = 0.00064516
    #             elif self.rate_unit == "Square Mile":
    #                 self.conversion_factor_between_area_and_rate = 4014489600
    #             elif self.rate_unit == "Square Yard":
    #                 self.conversion_factor_between_area_and_rate = 1296

    #         elif self.area_unit == 'Square Kilometer':
    #             if self.rate_unit == "Square Centimeter":
    #                 self.conversion_factor_between_area_and_rate = 1e-10
    #             elif self.rate_unit == "Square Foot":
    #                 self.conversion_factor_between_area_and_rate = 1.076e+7
    #             elif self.rate_unit == "Square Inch":
    #                 self.conversion_factor_between_area_and_rate = 1.55e+9
    #             elif self.rate_unit == "Square Kilometer":
    #                 self.conversion_factor_between_area_and_rate = 1
    #             elif self.rate_unit == "Square Meter":
    #                 self.conversion_factor_between_area_and_rate = 1000000
    #             elif self.rate_unit == "Square Mile":
    #                 self.conversion_factor_between_area_and_rate = 2.59
    #             elif self.rate_unit == "Square Yard":
    #                 self.conversion_factor_between_area_and_rate = 1.196e+6

    #         elif self.area_unit == 'Square Mile':
    #             if self.rate_unit == "Square Centimeter":
    #                 self.conversion_factor_between_area_and_rate = 3.86e-11
    #             elif self.rate_unit == "Square Foot":
    #                 self.conversion_factor_between_area_and_rate = 3.587e+7
    #             elif self.rate_unit == "Square Inch":
    #                 self.conversion_factor_between_area_and_rate = 5.34e+9
    #             elif self.rate_unit == "Square Kilometer":
    #                 self.conversion_factor_between_area_and_rate = 3.861e+6
    #             elif self.rate_unit == "Square Meter":
    #                 self.conversion_factor_between_area_and_rate = 2589988.11
    #             elif self.rate_unit == "Square Mile":
    #                 self.conversion_factor_between_area_and_rate = 1
    #             elif self.rate_unit == "Square Yard":
    #                 self.conversion_factor_between_area_and_rate = 3.098e+6

    #         elif self.area_unit == 'Square Yard':
    #             if self.rate_unit == "Square Centimeter":
    #                 self.conversion_factor_between_area_and_rate = 0.000119599
    #             elif self.rate_unit == "Square Foot":
    #                 self.conversion_factor_between_area_and_rate = 1
    #             elif self.rate_unit == "Square Inch":
    #                 self.conversion_factor_between_area_and_rate = 144
    #             elif self.rate_unit == "Square Kilometer":
    #                 self.conversion_factor_between_area_and_rate = 8.361e-7
    #             elif self.rate_unit == "Square Meter":
    #                 self.conversion_factor_between_area_and_rate = 0.83612736
    #             elif self.rate_unit == "Square Mile":
    #                 self.conversion_factor_between_area_and_rate = 3.2283e-7
    #             elif self.rate_unit == "Square Yard":
    #                 self.conversion_factor_between_area_and_rate = 1

    #         self.deal_value = self.rate * self.area  * self.conversion_factor_between_area_and_rate
    #         if int(self.deal_value) > 0:
    #             self.fees_amount = self.deal_value * (self._of_deal_value/100)
    def before_save(self):
        if self.deal_type == 'Outright/Sale' and self.area and self.rate:
            # Define conversion factors for different combinations of area and rate units
            conversion_factors = {
                'Square Meter': {
                    'Square Centimeter': 0.0001,
                    'Square Foot': 0.09290304,
                    'Square Inch': 0.00064516,
                    'Square Kilometer': 1000000,
                    'Square Meter': 1,
                    'Square Mile': 2589988.11,
                    'Square Yard': 0.83612736
                },
                'Square Centimeter': {
                    'Square Centimeter': 1,
                    'Square Foot': 929.0304,
                    'Square Inch': 645.16,
                    'Square Kilometer': 10000000000,
                    'Square Meter': 10000,
                    'Square Mile': 2.59e+10,
                    'Square Yard': 8361.2736
                },
                'Square Foot': {
                    'Square Centimeter': 1.07639104e-5,
                    'Square Foot': 1,
                    'Square Inch': 0.00694444,
                    'Square Kilometer': 92903.04,
                    'Square Meter': 0.09290304,
                    'Square Mile': 27878400,
                    'Square Yard': 9
                },
                'Square Inch': {
                    'Square Centimeter': 0.00064516,
                    'Square Foot': 144,
                    'Square Inch': 1,
                    'Square Kilometer': 6451600,
                    'Square Meter': 0.00064516,
                    'Square Mile': 4014489600,
                    'Square Yard': 1296
                },
                'Square Kilometer': {
                    'Square Centimeter': 1e-10,
                    'Square Foot': 1.076e+7,
                    'Square Inch': 1.55e+9,
                    'Square Kilometer': 1,
                    'Square Meter': 1000000,
                    'Square Mile': 2.59,
                    'Square Yard': 1.196e+6
                },
                'Square Mile': {
                    'Square Centimeter': 3.86e-11,
                    'Square Foot': 3.587e+7,
                    'Square Inch': 5.34e+9,
                    'Square Kilometer': 3.861e+6,
                    'Square Meter': 2589988.11,
                    'Square Mile': 1,
                    'Square Yard': 3.098e+6
                },
                'Square Yard': {
                    'Square Centimeter': 0.000119599,
                    'Square Foot': 1,
                    'Square Inch': 144,
                    'Square Kilometer': 8.361e-7,
                    'Square Meter': 0.83612736,
                    'Square Mile': 3.2283e-7,
                    'Square Yard': 1
                }
            }

            conversion_factor = conversion_factors.get(self.area_unit, {}).get(self.rate_unit)

            self.conversion_factor_between_area_and_rate = conversion_factor if conversion_factor is not None else None

            if self.conversion_factor_between_area_and_rate is not None:
                self.deal_value = self.rate * self.area * self.conversion_factor_between_area_and_rate
                if self.deal_value > 0:
                    self.fees_amount = self.deal_value * (self._of_deal_value / 100)
    
        elif self.deal_type == 'Lease' and self.rate_per_month and self.expected_tenure_in_months:
            self.deal_value = self.rate_per_month * self.expected_tenure_in_months 
            if int(self.deal_value) > 0:
                self.fees_amount = self.deal_value * self.no_of_months_of_rentals 
        elif self.deal_type == 'Co-working/Workstations' and self.expected_tenure_in_months and self.no_of_seats and self.rate_per_month_per_seat:
            self.deal_value = self.no_of_seats * self.rate_per_month_per_seat * self.expected_tenure_in_months
            if int(self.deal_value) > 0:
                self.fees_amount = self.deal_value * self.no_of_months_of_rentals 
        # else:
        #     missing_fields = []
        #     if not self._of_deal_valueno_of_months_of_rentals:
        #         missing_fields.append("Number of months of rentals")
        #     if not self.rate_unitrate_per_month:
        #         missing_fields.append("Rate per month")
        #     if not self.rateexpected_tenure_in_months:
        #         missing_fields.append("Expected tenure in months")
            
        #     if missing_fields:
        #         frappe.throw(f"Please enter the following required fields: {', '.join(missing_fields)}")



# @frappe.whitelist()
# def get_uoms(doctype, txt, searchfield, start, page_len, filters):
#     uoms = frappe.get_all(
#         'UOM',
#         filters={'name': 'Square Foot'},
#         fields=['name']
#     )

#     return [[uom['name']] for uom in uoms]

# @frappe.whitelist()
# def get_uoms(doctype, txt, searchfield, start, page_len, filters):
#     uoms = frappe.get_all(
#         'UOM',
#         filters={'name': ['in', ['Square Foot', 'Square Meter','Square Kilometer','Square Yard','Square Inch','Square Centimeter','Square Mile']]},  # Use 'in' operator to specify multiple values
#         fields=['name']
#     )

#     return [[uom['name']] for uom in uoms]
