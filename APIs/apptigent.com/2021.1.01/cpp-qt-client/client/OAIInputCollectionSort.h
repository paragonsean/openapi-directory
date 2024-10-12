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
 * OAIInputCollectionSort.h
 *
 * 
 */

#ifndef OAIInputCollectionSort_H
#define OAIInputCollectionSort_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInputCollectionSort : public OAIObject {
public:
    OAIInputCollectionSort();
    OAIInputCollectionSort(QString json);
    ~OAIInputCollectionSort() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getInput() const;
    void setInput(const QList<QString> &input);
    bool is_input_Set() const;
    bool is_input_Valid() const;

    QString getOrder() const;
    void setOrder(const QString &order);
    bool is_order_Set() const;
    bool is_order_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_input;
    bool m_input_isSet;
    bool m_input_isValid;

    QString m_order;
    bool m_order_isSet;
    bool m_order_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInputCollectionSort)

#endif // OAIInputCollectionSort_H
