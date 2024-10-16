/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITimezoneViewModel.h
 *
 * 
 */

#ifndef OAITimezoneViewModel_H
#define OAITimezoneViewModel_H

#include <QJsonObject>

#include "OAITimezonesViewModel.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITimezonesViewModel;

class OAITimezoneViewModel : public OAIObject {
public:
    OAITimezoneViewModel();
    OAITimezoneViewModel(QString json);
    ~OAITimezoneViewModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getObject() const;
    void setObject(const QString &object);
    bool is_object_Set() const;
    bool is_object_Valid() const;

    QList<QString> getRegions() const;
    void setRegions(const QList<QString> &regions);
    bool is_regions_Set() const;
    bool is_regions_Valid() const;

    QList<OAITimezonesViewModel> getTimezones() const;
    void setTimezones(const QList<OAITimezonesViewModel> &timezones);
    bool is_timezones_Set() const;
    bool is_timezones_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_object;
    bool m_object_isSet;
    bool m_object_isValid;

    QList<QString> m_regions;
    bool m_regions_isSet;
    bool m_regions_isValid;

    QList<OAITimezonesViewModel> m_timezones;
    bool m_timezones_isSet;
    bool m_timezones_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITimezoneViewModel)

#endif // OAITimezoneViewModel_H
