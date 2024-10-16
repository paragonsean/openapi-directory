/**
 * Background Removal API
 * Remove the background of any image
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_removebg_post_402_response_errors_inner.h
 *
 * 
 */

#ifndef OAI_removebg_post_402_response_errors_inner_H
#define OAI_removebg_post_402_response_errors_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_removebg_post_402_response_errors_inner : public OAIObject {
public:
    OAI_removebg_post_402_response_errors_inner();
    OAI_removebg_post_402_response_errors_inner(QString json);
    ~OAI_removebg_post_402_response_errors_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_removebg_post_402_response_errors_inner)

#endif // OAI_removebg_post_402_response_errors_inner_H
