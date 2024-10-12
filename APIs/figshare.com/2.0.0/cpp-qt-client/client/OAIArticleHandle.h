/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIArticleHandle.h
 *
 * 
 */

#ifndef OAIArticleHandle_H
#define OAIArticleHandle_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIArticleHandle : public OAIObject {
public:
    OAIArticleHandle();
    OAIArticleHandle(QString json);
    ~OAIArticleHandle() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getHandle() const;
    void setHandle(const QString &handle);
    bool is_handle_Set() const;
    bool is_handle_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_handle;
    bool m_handle_isSet;
    bool m_handle_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIArticleHandle)

#endif // OAIArticleHandle_H
