

# EmployeeEmergencyContactsInner

The emergency contact model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address1** | **String** | 1st address line. |  [optional] |
|**address2** | **String** | 2nd address line. |  [optional] |
|**city** | **String** | City. |  [optional] |
|**country** | **String** | County. |  [optional] |
|**county** | **String** | Country.  Must be a valid 3 character country code.  Common values are *USA* (United States), *CAN* (Canada). |  [optional] |
|**email** | **String** | Contact email.  Must be valid email address format. |  [optional] |
|**firstName** | **String** | Required. Contact first name. &lt;br  /&gt;Max length: 40 |  |
|**homePhone** | **String** | Contact Home Phone.  Valid phone format  *(###) #######* or *######-####* or *### ### ####* or *##########* or, if international, starts with *+#*, only spaces and digits allowed. |  [optional] |
|**lastName** | **String** | Required. Contact last name. &lt;br  /&gt;Max length: 40 |  |
|**mobilePhone** | **String** | Contact Mobile Phone.  Valid phone format  *(###) #######* or *######-####* or *### ### ####* or *##########* or, if international, starts with *+#*, only spaces and digits allowed. |  [optional] |
|**notes** | **String** | Notes. &lt;br  /&gt;Max length: 1000 |  [optional] |
|**pager** | **String** | Contact Pager.  Valid phone format  *(###) #######* or *######-####* or *### ### ####* or *##########* or, if international, starts with *+#*, only spaces and digits allowed. |  [optional] |
|**primaryPhone** | **String** | Required. Contact primary phone type.  Must match Company setup.  Valid  values are H (Home), M (Mobile), P (Pager), W (Work) |  [optional] |
|**priority** | **String** | Required. Contact priority. Valid values are *P* (Primary) or *S* (Secondary). |  [optional] |
|**relationship** | **String** | Required. Contact relationship.  Must match Company setup.  Common values are Spouse, Mother, Father. |  [optional] |
|**state** | **String** | State or Province.  If U.S. address, must be valid 2 character state code.  Common values are *IL* (Illinois), *CA* (California). |  [optional] |
|**syncEmployeeInfo** | **Boolean** | Valid values are *true* or *false*. |  [optional] |
|**workExtension** | **String** | Work Extension. |  [optional] |
|**workPhone** | **String** | Contact Work Phone.  Valid phone format  *(###) #######* or *######-####* or *### ### ####* or *##########* or, if international, starts with *+#*, only spaces and digits allowed. |  [optional] |
|**zip** | **String** | Postal code.  If U.S. address, must be a valid zip code. |  [optional] |



