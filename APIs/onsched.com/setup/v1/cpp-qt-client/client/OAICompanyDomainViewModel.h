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
 * OAICompanyDomainViewModel.h
 *
 * 
 */

#ifndef OAICompanyDomainViewModel_H
#define OAICompanyDomainViewModel_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICompanyDomainViewModel : public OAIObject {
public:
    OAICompanyDomainViewModel();
    OAICompanyDomainViewModel(QString json);
    ~OAICompanyDomainViewModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDomain() const;
    void setDomain(const QString &domain);
    bool is_domain_Set() const;
    bool is_domain_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getObject() const;
    void setObject(const QString &object);
    bool is_object_Set() const;
    bool is_object_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_domain;
    bool m_domain_isSet;
    bool m_domain_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_object;
    bool m_object_isSet;
    bool m_object_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICompanyDomainViewModel)

#endif // OAICompanyDomainViewModel_H
