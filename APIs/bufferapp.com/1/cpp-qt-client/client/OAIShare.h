/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIShare.h
 *
 * 
 */

#ifndef OAIShare_H
#define OAIShare_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIShare : public OAIObject {
public:
    OAIShare();
    OAIShare(QString json);
    ~OAIShare() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isSuccess() const;
    void setSuccess(const bool &success);
    bool is_success_Set() const;
    bool is_success_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_success;
    bool m_success_isSet;
    bool m_success_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIShare)

#endif // OAIShare_H
