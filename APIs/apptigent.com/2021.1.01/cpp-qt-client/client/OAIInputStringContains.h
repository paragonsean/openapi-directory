/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIInputStringContains.h
 *
 * 
 */

#ifndef OAIInputStringContains_H
#define OAIInputStringContains_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInputStringContains : public OAIObject {
public:
    OAIInputStringContains();
    OAIInputStringContains(QString json);
    ~OAIInputStringContains() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFind() const;
    void setFind(const QString &find);
    bool is_find_Set() const;
    bool is_find_Valid() const;

    QString getInput() const;
    void setInput(const QString &input);
    bool is_input_Set() const;
    bool is_input_Valid() const;

    QString getLower() const;
    void setLower(const QString &lower);
    bool is_lower_Set() const;
    bool is_lower_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_find;
    bool m_find_isSet;
    bool m_find_isValid;

    QString m_input;
    bool m_input_isSet;
    bool m_input_isValid;

    QString m_lower;
    bool m_lower_isSet;
    bool m_lower_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInputStringContains)

#endif // OAIInputStringContains_H
