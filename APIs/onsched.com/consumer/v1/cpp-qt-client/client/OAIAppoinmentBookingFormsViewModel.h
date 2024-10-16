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
 * OAIAppoinmentBookingFormsViewModel.h
 *
 * 
 */

#ifndef OAIAppoinmentBookingFormsViewModel_H
#define OAIAppoinmentBookingFormsViewModel_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAppoinmentBookingFormsViewModel : public OAIObject {
public:
    OAIAppoinmentBookingFormsViewModel();
    OAIAppoinmentBookingFormsViewModel(QString json);
    ~OAIAppoinmentBookingFormsViewModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBookingConfirmationPage() const;
    void setBookingConfirmationPage(const QString &booking_confirmation_page);
    bool is_booking_confirmation_page_Set() const;
    bool is_booking_confirmation_page_Valid() const;

    QString getBookingForm() const;
    void setBookingForm(const QString &booking_form);
    bool is_booking_form_Set() const;
    bool is_booking_form_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_booking_confirmation_page;
    bool m_booking_confirmation_page_isSet;
    bool m_booking_confirmation_page_isValid;

    QString m_booking_form;
    bool m_booking_form_isSet;
    bool m_booking_form_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppoinmentBookingFormsViewModel)

#endif // OAIAppoinmentBookingFormsViewModel_H
