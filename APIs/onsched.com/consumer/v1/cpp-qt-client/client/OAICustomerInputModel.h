/**
 * OnSched Consumer API
 * Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICustomerInputModel.h
 *
 * 
 */

#ifndef OAICustomerInputModel_H
#define OAICustomerInputModel_H

#include <QJsonObject>

#include "OAIAddressInputModel.h"
#include "OAIContactInputModel.h"
#include "OAICustomFieldInputModel.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAddressInputModel;
class OAIContactInputModel;
class OAICustomFieldInputModel;

class OAICustomerInputModel : public OAIObject {
public:
    OAICustomerInputModel();
    OAICustomerInputModel(QString json);
    ~OAICustomerInputModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAddressInputModel getAddress() const;
    void setAddress(const OAIAddressInputModel &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    OAIContactInputModel getContact() const;
    void setContact(const OAIContactInputModel &contact);
    bool is_contact_Set() const;
    bool is_contact_Valid() const;

    OAICustomFieldInputModel getCustomFields() const;
    void setCustomFields(const OAICustomFieldInputModel &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getFirstname() const;
    void setFirstname(const QString &firstname);
    bool is_firstname_Set() const;
    bool is_firstname_Valid() const;

    QString getLastname() const;
    void setLastname(const QString &lastname);
    bool is_lastname_Set() const;
    bool is_lastname_Valid() const;

    QString getLocationId() const;
    void setLocationId(const QString &location_id);
    bool is_location_id_Set() const;
    bool is_location_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getNotificationType() const;
    void setNotificationType(const QString &notification_type);
    bool is_notification_type_Set() const;
    bool is_notification_type_Valid() const;

    bool isSendLeadNotification() const;
    void setSendLeadNotification(const bool &send_lead_notification);
    bool is_send_lead_notification_Set() const;
    bool is_send_lead_notification_Valid() const;

    QString getStripeCustomerId() const;
    void setStripeCustomerId(const QString &stripe_customer_id);
    bool is_stripe_customer_id_Set() const;
    bool is_stripe_customer_id_Valid() const;

    qint32 getType() const;
    void setType(const qint32 &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAddressInputModel m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    OAIContactInputModel m_contact;
    bool m_contact_isSet;
    bool m_contact_isValid;

    OAICustomFieldInputModel m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_firstname;
    bool m_firstname_isSet;
    bool m_firstname_isValid;

    QString m_lastname;
    bool m_lastname_isSet;
    bool m_lastname_isValid;

    QString m_location_id;
    bool m_location_id_isSet;
    bool m_location_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_notification_type;
    bool m_notification_type_isSet;
    bool m_notification_type_isValid;

    bool m_send_lead_notification;
    bool m_send_lead_notification_isSet;
    bool m_send_lead_notification_isValid;

    QString m_stripe_customer_id;
    bool m_stripe_customer_id_isSet;
    bool m_stripe_customer_id_isValid;

    qint32 m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICustomerInputModel)

#endif // OAICustomerInputModel_H
