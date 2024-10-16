/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILiabilitiesModel.h
 *
 * 
 */

#ifndef OAILiabilitiesModel_H
#define OAILiabilitiesModel_H

#include <QJsonObject>

#include "OAIILiability.h"
#include "OAIObjectLink.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIILiability;
class OAIObjectLink;

class OAILiabilitiesModel : public OAIObject {
public:
    OAILiabilitiesModel();
    OAILiabilitiesModel(QString json);
    ~OAILiabilitiesModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIILiability> getLiabilities() const;
    void setLiabilities(const QList<OAIILiability> &liabilities);
    bool is_liabilities_Set() const;
    bool is_liabilities_Valid() const;

    QList<OAIObjectLink> getLinks() const;
    void setLinks(const QList<OAIObjectLink> &links);
    bool is_links_Set() const;
    bool is_links_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIILiability> m_liabilities;
    bool m_liabilities_isSet;
    bool m_liabilities_isValid;

    QList<OAIObjectLink> m_links;
    bool m_links_isSet;
    bool m_links_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILiabilitiesModel)

#endif // OAILiabilitiesModel_H
