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
 * OAIInputCurrencyFormat.h
 *
 * 
 */

#ifndef OAIInputCurrencyFormat_H
#define OAIInputCurrencyFormat_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInputCurrencyFormat : public OAIObject {
public:
    OAIInputCurrencyFormat();
    OAIInputCurrencyFormat(QString json);
    ~OAIInputCurrencyFormat() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getInput() const;
    void setInput(const double &input);
    bool is_input_Set() const;
    bool is_input_Valid() const;

    QString getTarget() const;
    void setTarget(const QString &target);
    bool is_target_Set() const;
    bool is_target_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_input;
    bool m_input_isSet;
    bool m_input_isValid;

    QString m_target;
    bool m_target_isSet;
    bool m_target_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInputCurrencyFormat)

#endif // OAIInputCurrencyFormat_H
