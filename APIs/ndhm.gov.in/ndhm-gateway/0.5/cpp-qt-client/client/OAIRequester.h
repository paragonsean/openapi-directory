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
 * OAIRequester.h
 *
 * 
 */

#ifndef OAIRequester_H
#define OAIRequester_H

#include <QJsonObject>

#include "OAIRequester_identifier.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIRequester_identifier;

class OAIRequester : public OAIObject {
public:
    OAIRequester();
    OAIRequester(QString json);
    ~OAIRequester() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIRequester_identifier getIdentifier() const;
    void setIdentifier(const OAIRequester_identifier &identifier);
    bool is_identifier_Set() const;
    bool is_identifier_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIRequester_identifier m_identifier;
    bool m_identifier_isSet;
    bool m_identifier_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRequester)

#endif // OAIRequester_H
