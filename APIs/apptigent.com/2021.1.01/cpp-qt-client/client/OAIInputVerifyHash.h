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
 * OAIInputVerifyHash.h
 *
 * 
 */

#ifndef OAIInputVerifyHash_H
#define OAIInputVerifyHash_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInputVerifyHash : public OAIObject {
public:
    OAIInputVerifyHash();
    OAIInputVerifyHash(QString json);
    ~OAIInputVerifyHash() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAlgorithm() const;
    void setAlgorithm(const QString &algorithm);
    bool is_algorithm_Set() const;
    bool is_algorithm_Valid() const;

    QString getHash() const;
    void setHash(const QString &hash);
    bool is_hash_Set() const;
    bool is_hash_Valid() const;

    QString getInput() const;
    void setInput(const QString &input);
    bool is_input_Set() const;
    bool is_input_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_algorithm;
    bool m_algorithm_isSet;
    bool m_algorithm_isValid;

    QString m_hash;
    bool m_hash_isSet;
    bool m_hash_isValid;

    QString m_input;
    bool m_input_isSet;
    bool m_input_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInputVerifyHash)

#endif // OAIInputVerifyHash_H
