/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIConsentArtefactReference.h
 *
 * 
 */

#ifndef OAIConsentArtefactReference_H
#define OAIConsentArtefactReference_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIConsentArtefactReference : public OAIObject {
public:
    OAIConsentArtefactReference();
    OAIConsentArtefactReference(QString json);
    ~OAIConsentArtefactReference() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConsentArtefactReference)

#endif // OAIConsentArtefactReference_H
