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
 * OAICurationCommentCreate.h
 *
 * 
 */

#ifndef OAICurationCommentCreate_H
#define OAICurationCommentCreate_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICurationCommentCreate : public OAIObject {
public:
    OAICurationCommentCreate();
    OAICurationCommentCreate(QString json);
    ~OAICurationCommentCreate() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getText() const;
    void setText(const QString &text);
    bool is_text_Set() const;
    bool is_text_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_text;
    bool m_text_isSet;
    bool m_text_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICurationCommentCreate)

#endif // OAICurationCommentCreate_H
