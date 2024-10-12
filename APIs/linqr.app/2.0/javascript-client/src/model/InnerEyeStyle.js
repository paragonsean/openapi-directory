/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import InnerEyeShapes from './InnerEyeShapes';

/**
 * The InnerEyeStyle model module.
 * @module model/InnerEyeStyle
 * @version 2.0
 */
class InnerEyeStyle {
    /**
     * Constructs a new <code>InnerEyeStyle</code>.
     * @alias module:model/InnerEyeStyle
     */
    constructor() { 
        
        InnerEyeStyle.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>InnerEyeStyle</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InnerEyeStyle} obj Optional instance to populate.
     * @return {module:model/InnerEyeStyle} The populated <code>InnerEyeStyle</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InnerEyeStyle();

            if (data.hasOwnProperty('color')) {
                obj['color'] = ApiClient.convertToType(data['color'], 'String');
            }
            if (data.hasOwnProperty('shape')) {
                obj['shape'] = ApiClient.convertToType(data['shape'], InnerEyeShapes);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>InnerEyeStyle</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>InnerEyeStyle</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['color'] && !(typeof data['color'] === 'string' || data['color'] instanceof String)) {
            throw new Error("Expected the field `color` to be a primitive type in the JSON string but got " + data['color']);
        }

        return true;
    }


}



/**
 * Base color for inner QR Code eyes. If this value is not specified, the inner eyes are styled according to the modules color configuration.
 * @member {String} color
 */
InnerEyeStyle.prototype['color'] = undefined;

/**
 * You can choose from following inner eye shapes:  |Value | Preview| |---:|:---| |`circle`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAACdElEQVR4nO3bSW4TQRTG8T+wY5AgLIIIWYWYHbBFiXICRgkhseEkyGE4ABGXiJhWzGcAhWFFbkAWmCCGVWJYdCzFlo3jTtf3quPvJ72NN6/eq3Z1u1wNZmZmZmZmZmZmZmZmZmZmZmZmZmaV2Rc9gBFNAOeBBjAJHNz6/A+wBqwCn4BWyOj2qAZwH/gAbAJ/h8QmsALcA2YDxrtnLABvGN7wYfEamBePvdamgafsvvG98RiYEtZRS1co1u+qm9+JH8ANWTU1c5d0jd8ebWBRVFNtPETT/O2xJKmsBlRXfr9oCurL2iWKJSFqAtrAteRVZmoa+E5c8zvRYkyfjp4R3/xOPEpca3YWiG96b8wlrTgzb4lveG+8SlpxRmaJvfH+LxoJ6+5rvzohcIt8d2FvRg9A4SPxV/qgeJew7iwcZ2dbylGxARxLVn0f6iXoXEDOURwAzioTqpshv8mVcEaZTD0BJ8T5yphUJlNPwCFxvjKOKJPlvB6PBfUE/BbnK+OnMpl6Ar6K85WxpkymnoBVcb4yvkQPIKUJ/EOsi/ob0AI+i3OOYoXiTyKZiKeg5wE5d+pF9AAUTpPndnQbmElYd1aqOHJYdYzF1d8xT3zDe+NC0ooz9IT4pndiOXGtWTpF2nOgO41vwMnEtWbrIvEHs64mrzJzi8RNwG1BfbWwhL75DySV1UgTzXLUxlf+QJcpboqpmr8OXJdVU1NTFGc1q27+MmP8tFPGHMVxwd0sS23gJWP4I6tKM8Ad4D3FdvGwpm9QHLBqUoO9nVyPCA5ylO4XtQ9vff6L7he110NGZ2ZmZmZmZmZmZmZmZmZmZmZmZmYW6x9vJn78f9r/5gAAAABJRU5ErkJggg==\" alt=\"circle inner eyes shape\" title=\"circle inner eyes shape preview\"> | |`cushion`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAACSElEQVR4nO3bPW4TURSG4RdDCQEhUcACCCnBXQqQ0rAI1gSrYAf0SFCTBBr+GjroACnpkALFeLBjYaPJxOe7Ut5HGimKFZ+T+2XuiRNfkCRJkiRJkiRJkiRJkiRJOjeXi+vtAbvAL+A78Lu4/ioTYBt4DNwCvlQVvlJVaOY28Hz28THwDthfuD4AJwV93AGmC9cucHP22JOC+n9dqiwG3KNb5FU2Ecq6xV7V46cR9QapDmAC/AC2BnzNkFCGLvayI+DGiufeiOoAAF4BD0c+xxFwSBcGdIt9H7g28nlfA49GPkfzntEN3xavpxv8vv9pUl2Q+U9ti8p7M4DTyntLzICzDOIK5QMYMnfACfA2UPd/DihefMgEAG1uQ5GeDGDOAMIiPSWGMLQ3iCMDGHJ3QGuD+JDA4kMuAGhrG3qTKmwAnVgvBtCJ9ZIawtDOII4NYMjeAa0M4sgr4F4yAGhjG4r2kA4guQX2oj2kA5iG60O4h/QQ/sn4fyOOdQxc5wIO4W3yiw9wFbibKp4MoIXtpxfrxQA6FzKAB8Hay2IBJP8c3cIA7sUGceoOaGUA92KDOBVAS/t/L9KTAcwZQFikp9Qbs1oawL3IIE7cAa0N4F5kECcCaHH76ZX3ZgCnlfdWfUYMzucV8KYOaJQHkDiiNHQAVx5RKh/E1QHsAO/XPN7CIb0d4OOIeoNUb0GLt3jVMdWvs+vFwufWhTKlMIDqO2CP7qzwPvCZ4LsRlkzofgWdAt+Al9l2JEmSJEmSJEmSJEmSJEmSzuQPiB+iRrGkHEcAAAAASUVORK5CYII=\" alt=\"cushion inner eyes shape\" title=\"cushion inner eyes shape preview\"> | |`default`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAuUlEQVR4nO3bsQlCARAFwVPs6xdhHZZmEXZmYmiiyC3CTAPvYOObAQAAAAAAAAAAAPiZ0/LedWaO5c1PPWbmvjV22Rp6OWbmtrz5jbUA560h3hMgJkBMgJgAMQFiAsQEiAkQEyAmQEyAmAAxAWICxASICRATICZATICYADEBYgLEBIgJEBMgJkBMgJgAMQFiAsQEiAkQEyAmQEyAmAAxAWICxLb/hB/Le9/4hxsBAAAAAAAAAAAA3nkCLnsFM1ox7dEAAAAASUVORK5CYII=\" alt=\"default inner eyes shape\" title=\"default inner eyes shape preview\"> | |`diamond`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAABeklEQVR4nO3aO0ptMRhA4eWjE1sdg+AcLogjsHEaDkVnY6Fg5RQuVnaCcxC02IqWgiH5H+uD0ybZLJJ92AQkSZIkSZIkSZIkSZIkSZKG2Zk83yVwNnjMa+D/4DHLugHeB/9egdOZDzHS7uoFDHAE3JM0QoUAkDhClQCQNEKlAJAwQrUAkCxCxQCQKELVAJAkQuUAkCBC9QAQPEKHABA4QpcAEDRCpwAQMEK3ALBFuANOVi8EegYAOAYeCLATugaAIMdR5wAQIEL3ALA4ggE2yyIY4NuSCHszJwOegQvgcPK8v3UAvAG3syacvQOe2G5FvEyeN6wVR5ARflj1DjDCp5UvYSOw/l9Q+wirA8AW4Zzthls7EQLAdrfzHw13QpQA0PQ4ihQAGkaIFgCaRYgYABpFiBoAmkSIHAAaRIgeAIpHyBAACkfIEgCKRsgUAApGyBYAikXIGAAKRdhfvYA/+PqKejV43MfB40mSJEmSJEmSJEmSJEmSJM3yATM2Vjf/WCn/AAAAAElFTkSuQmCC\" alt=\"diamond inner eyes shape\" title=\"diamond inner eyes shape preview\"> | |`dots`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAAFIUlEQVR4nO2b228VRRjAf0oV2hMtxQYbNN4tgUKtJAKKGgPxwTv4YOKdYJqghieJfwHqs2lqfAcFbUIwxivXqAkmhMbEVNSIxcSeVEzaHkSUtnF9+LZhz7Jnd+fjnD2375fMQ5P+zuzMnDPzzTezYBiGYRiGYRiGYRiGYRiGYRiGYRiGYRiGYRiGYRiGUTYuq3L9bcCDwB1ADsgDh4DvE7wu4BHgZv/vX4FPgfEEbyWwHlgC/A18B+wH/lE8e92zFfgT8CLKAaA7wskBg8B0hDMNDPj/E2YpcLBEXaeB/jK1qW4YJLozgmUSWBNwFgLDKbzjQHvAW+t/VpI3UPZW1ihbSe6MuZIHOnxvn4O313cWIdNSWq/hfwltyE8+bYd4wBvA/Y6OB9wLvOXo/AG0Vqz1NcATuHfkKPCuwnsH+E3hPVax1kdweZaVAX0K5ybgAYW3HrhB4WmeUU3WAxAVoaShKyMH4CqlpyLrAcgrnFkk+nFl2Hdd+V3hqMl6AA4qnK+AzxTeJ8A3Ck/zjHXFftwWxUeBTmDKwZkErgE2Otb1RQXbXTN0k25j5AHvB7wXUzoe8HzA25PSmQBuL3Nba5Y1yHqQ1PkLQt6rwEyMMw28HHIWALsT6hoD7ipj++qCDmSTNcqFjphB5uC4WHw5sIviKWkK2Aksi/Ee9z87OICjwA4kzVEV5lWrYuBfJEpp88t84Fvgc+Bj4FwJbwr5Vl+BDOJZ4DCy6H4N/FfCm0BCzPlIiuIkMiD7gJ8vuTV1xkLgI0pPCQVkzg/TB/wU4/0I9EZ4m/3PLOXtpTiB19DkSJfV9JA5f44+4K8UzhmKB2FbyrqOo98o1hVpUtHBNWE5Mt3EffPD5QTQAqwgftEOl4ZPSXcRfZgSV3YBzzk6HvAMEkm5ONPAtRVrfQRZL8JPAZscnRuBK5Ffggse8BCy6KZlHjCCHFVmQtapiFsVTjtwt8K7B7ha4d2mcNRkPQBavIycS/FUZD0AvyicArI/cOUoEhG5onnGukGzCO8EnnV0POBp4D1H5zywuGKtrxEGcItKliFh6AkHbwQJQ3twC0PfrmC7a4YcsulJ0yHBxFovMqUkOQUk/p/jlZR1HUNSIk1BO7L9L9UZk0jsH6aX+F/CCHL7LcwLxJ8nDKGLmOqedcjthR+Qb+4h4DXkMKUULcgmawhJaeeBD5E5vyXG6wS2+3UU/DoHkXC1KVmE3NsJXh2ZRTKbG2O8FcgON5hcKyALbk+Mt8n/7NmAdwp403+WpmItyTfW9nDxgcw24hfVGWTOD9IKfJBQVx5YXcb21TRLSX8kuTvgbU7peMicD3L7O6nz58oE0ReCG44DpO9IDznJ6iQ+nx8uZ5B4/knHug5XsN01wUrcOsRDFs3XFd524IjCi1tHyk5c1FAJNiic+9C9SPIwEmW5sgEJZzMh61zQEoXTAtyp8Fah+4Jdr3DUZD0AZ5XeWEYO6BJ4arIeAM1BxynkeqIrR5A9hiuZHcZUg1bcX9DYgawDrovpOmST5eKMc/Heo+HoJ32HjHHh0lRc7ihchnyng+QbeMGypSItrkHSpKQnKL4u2E66LOoxihNrq/3PSvKaIhUdpB95JyuqM74k+qJsDhm8qEOd80gnRqWUuyl9K3sceKlMbXKm2i9qtyJx9yqk4/LIdcGkOHwx8qL2Lf7fJ5EXtU8neD1+fdchL2oP+/U15YvahmEYhmEYhmEYhmEYhmEYhmEYhmEYhmEYhmEYhmE0HP8DPs5w2PDzewAAAAAASUVORK5CYII=\" alt=\"dots inner eyes shape\" title=\"dots inner eyes shape preview\"> | |`heavyround`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAACBklEQVR4nO3bTU4UURSG4bedMGljnChMWIcQ1DUorMGBRqeuQsIKcBGgJg4cmICwDUj8m2iihg5N1EGlGHTSgS7rnnOx3yc50z733K9TqequC5IkSZIkSZIkSZIkSZIkSb0ZZC9giuvAPWAZWARuAddm/IzfwFfgM3AEvAd+9LjG/84A2ABeAyPgT881Al4B69T7xUuzBhzS/6ZPqwNgNWSyK+ARcErc5rd1BjwPmK9qW8Rv/GRtFp+yUs/I3/y2nhSetTprwJj8jW9rDKwUnbgiA+AD+Zs+WYfMyd3RBvmbPa0eFpy7Gm/I3+hptVtw7ioMKfOQ1VeNaJ7Cw8z6eP+v7gMLwT1nsUBzgxAmOoDl4H5dhK4xOoCl4H5dhK4xOoAbwf26uBnZLDoATTCAZAaQzACSGUAyA0hmAMkMIJkBJDOAZAaQzACSGUCy6AC+B/fr4ltks+gAPgX36+JjZLPoAI6D+3VxFdbY2RA4If/P97n9U/4n8C645yzeEnyGIOMuaDuh52W9zF5AlD3yLzeTdcCcvJoIzeGIml7OPQXuFJ24Qk/J3/i2HheetVqb5G/+i+JTVi7riNIYjyidWyH2zMA+c3jNv8iA5v38Xco8rJ0AO8CDqIEuo9bbriFwl+ZF2SXgNt0Oan+h+f2pPaj9q8c1SpIkSZIkSZIkSZIkSZIk1eYvBAZ02jBVOVEAAAAASUVORK5CYII=\" alt=\"heavyround inner eyes shape\" title=\"heavyround inner eyes shape preview\"> | |`horizontal_lines`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAACqElEQVR4nO3bz2pTQRTH8W80caMVRU1QXFhc6LJWNz6AFPEBShE3/nkaEZHSF7D1CcRFfQE34p+VttVdKrQ0EbQuTFLrYlIpFy8lwTnnmPw+cBZZnTln7p3MneSCiIiIiIiIiIiIiIiIiIiIiIiIiMg/U/EeAFADLgJHjfP+AD4DXeO8YTSABeArsOsUbWAeqGeuNZwrwBf8Gl+MdWAqa8WBNIjV/P2TMBZ3wgL+zS6L+Yx1h1DDd80/KNr9MZo5ZJmMtNs5YZxzECeBScuE1hNgvdUcxoRlMusJWDfON4ym9wBye4f/Wl8WbzLWHcYc/o0ui9mMdYdRARbxb3YxnuYsOpoq8Ajo4d/4LvCwPyZz3odxl4E7pKMJ66fQTdKavwisGOf+w2XW91kDlknNaGC3K/sFbJAm4JNRznBuAqv4L0ErwEzmWsN5AOzg3/y92AHuZ604kGukLz7vphejA0xnrDuMF/g3uyyeZ6w7hOOkK8270WXxkxE/C5rE+Lh3QEeAC5YJrSdg1zjfMEzHaP0gNgG0iHsXdIBTwLZVQus74Dvw0jjnIJYxbL6XaWJ+EXcYo39G3CPWg1gPuJu14oBmSMcA3s3/CNzIXGsp79PQw8B14Co+h3GvgVf9zy68T0MvAbdIx9GnjXNvkSa9DXwwzu2uCjwmxg8yPdKPQ94Xo5kK8Az/xhdjCf8l2cRt/JtdFnMZ6w7jPf6NLou3GesO4Sz+TT4oGtmq/wvro4hzxvmGcd4ymfUE/A/nLN+8B5BTjbTv9l5myqKF8XbU+g7okragUS2RngtGWp30L2nvq70YTeBMxrpDmSLWJDQZo6PoPXXSO1me3wkt4AmOV36ER+8q6dWlY8Z5t0kvao/8mi8iIiIiIiIiIiIiIiIiIiIiIiIiY+M3pp7y7rq742gAAAAASUVORK5CYII=\" alt=\"horizontal_lines inner eyes shape\" title=\"horizontal_lines inner eyes shape preview\"> | |`leaf`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAAB1UlEQVR4nO3bMU4UYRjG8T8TKJylADwCF7Ai3gGuQGej0Zgt5RaewFhqQ7yANYSC0MsFMJFGKCRRi8EQ1y1gw77Ph/v/JV/9fDvPzM7MZl+QJEmSJEmSJEmSJEmSJEm6N0vpDUyxCmwBm8D69VoDuqL8z8CHoqxmjICXwBFwBfwKrrdz/qx/Wa4Mm6IDxsAesBHeS0SygJ7hUt8J7iEuVUAHfAS2Q/nNqLqxTRrjwQcyBfTAm0BukxIFPAMeB3KblChgN5DZrOoCRsCT4symVRfwlPy7R1OqC9gszmtedQHrxXnNs4Cw6gIeFec1L/UmrGsWEGYBYRYQZgFhFhBmAWEWEGYBYRYQZgFhFhBmAWHVBVwW583ie2VYdQHnxXmzKN2jBfzrvy7gtDhvFqV7rJ4PGDGcYSvFubd1xTCLUHavqr4CLoCT4sy7OKb4QSHxGPo+kHlb79IbqNADX8lOwUxbZyzQnwbG5A/45Ho110/cmA74RP6g/1n7tDmwOFc9bZSwzwJ99UzqgNdk7glnDF87C3fmT9MDL4BD5jum+gM4AJ7TyFnfYvs9N4PaG9wMa9/1kfknw0vfOfAN+MIwh/wQfhCUJEmSJEmSJEmSJEmSJEmaxW+/AwgA5EQ11gAAAABJRU5ErkJggg==\" alt=\"leaf inner eyes shape\" title=\"leaf inner eyes shape preview\"> | |`left_eye`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAABjElEQVR4nO3bOy5EcRiG8cdE4Va4LMEGVGIPVEqJTikSJa0VSPQoqaxAqSBhA6xAQiMUk6A4RMYo+d5/4vklU79nzpO5nMkckCRJkiRJkiRJkiRJkiRJ+jUj6QP4wRSwCMwDMx+PaaBXtH8OnBRtNWMS2ASugD7wFnzs//FzHTBaOfaDHrAN7AKz4WOJSAaYoHuprwSPIS4VoAecAsuh/WZUfbB9t40nH8gEmAB2ArtNSgTYAOYCu01KBFgPbDarOsAksFC82bTqAEvkrz2aUh1gvnivedUBZor3mmeAsOoA48V7zUtdCeuDAcIMEGaAMAOEGSDMAGEGCDNAmAHCDBBmgDADhBlg2FPlmAGGPVaOGWCYAcLuKscMMKgPXFYOGmDQDfBcOWiAQYfVgwb4cg8cV48a4Mse8FI9aoDOGXCQGDZAd/LX6G7QK/efA9wDW8AqgbeeT//tn8p94Jruw/aI4In/VB3gAhgr2nql+1nhEXgAbunuQy79ni9JkiRJkiRJkiRJkiRJklToHRIyRdubyX/yAAAAAElFTkSuQmCC\" alt=\"left_eye inner eyes shape\" title=\"left_eye inner eyes shape preview\"> | |`lightround`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAABZ0lEQVR4nO3bMUpDQRRG4aNYmHQi6jIUt6BuRAlkOxJcjbgFyTKSKLY2QizSBR/ow3f/MZ4Ppr4zc3iEFAOSJEmSJEmSJEmSJEmSJEm/Zi88fwzcAOfAGXBQNPcDWAJz4BF4L5rblCnwAqzDawVMBj5rcx7IX/z2mg164oZMyV9219r5L2HM5pNPX3TXWgKjwU7/hf3KYWx+cE+KZ/7EKXBdObA6wEXxvD5K91gd4Kh4Xh/HlcOqA6T/d3xH6R6rA2iLAcIMEGaAMAOEGSDMAGEGCDNAmAHCDBBmgDADhBkgzABhBggzQJgBwgwQZoAwA4QZIMwAYQYIM0BYdYB18bw+SvdYHeCteF4fr5XDqgPMi+f18Rf22NuIth9oLIDDwU7fiAn5i+5atwOeuykz8pe9ve4HPXGDJmzeZKUvfgHcDXzWTukHEyPgCrgk81D7GXjinz7UliRJkiRJkiRJkiRJkiRJO+cTqys8yEZ91fkAAAAASUVORK5CYII=\" alt=\"lightround inner eyes shape\" title=\"lightround inner eyes shape preview\"> | |`right_eye`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAABiUlEQVR4nO3bPy5EYRxG4UNUaLAAhR1IWIAFSFSisgCRsAGlUjIbkKhEJbEAPZ2eHUhGM9OQobgEmYJi/N4vcZ7k1u+dOZP5l3tBkiRJkiRJkiRJkiRJkiRpYqaK97aBjaKtEfAE9N+Pe+AWGBTtN6kHvAaPZ7oIe8DcHz/WJqUDfD0egUNg+k8f8Q+i42FLwAlwCcymTuI/B/iwCZwTei4M0NkE9hPDBvh0ROCD2QCfFoHd6lEDfGeAsFVgvnLQAN/NAGuVgwYYt1I5ZoBxC5VjBhhngLDS3wIGCDNAmAHCDBBmgDADhBkgzABhBggzQJgBwgwQZoCw6gDD4r3mVQfoF+81zwBh1QEeiveaVx3ghu4Scb2rDjAA7oo3m5b4GnoW2GxWIsAp3c0RIhNgCBwHdpuU+iXcA65C201JBRgBOxgh+l/QENgCDvjHnwnpP+NGdG9Hy3S3jt4CL9EzKlZ9o/ZvzALrdFcpL9Jdq7lA3YvlGrgo2pIkSZIkSZIkSZIkSZIkSZqkN+iuaKbXQi61AAAAAElFTkSuQmCC\" alt=\"right_eye inner eyes shape\" title=\"right_eye inner eyes shape preview\"> | |`shield`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAACxklEQVR4nO3bS2sTURjG8b8piJUmbVWIdiG1uhEFRcGNgmsRbP0ablzrpxDEL+FGXLlQRFE3LSiCeMMLCPWCaK22NUgaXZwzVIekaWzmPEN5fvCSXnnOzHvOJJmZgJmZmZmZmZmZmZmZmZmZmZmZmZmZRbtjmcAW4B5wN35tCY0DM8DvWNPxZ1awCeAy0GBl52fViL/bIxvdBjQEnAQu8u+M71bTwIX4v0PJR92DTYnzBoE6UInfV2ONAtuA7YQZPAHsBfYBA+vMXAZexXob6wvwFZgDfsQCaAGfgJ/rzCytKdY+i1U1WdjWl0CFMBPVO7lTvWH9K64nle5/0lct4ErizF5cIhyyNrQqMI9+tufrO1ArcLvbSr0CIDzhXRPkdnOV0ISkFA0AuC7KXU0Zx1SYrcAi+sNOVotxTMmpVsAScFOU3c4NwpiSUzUA4JYwO++2KljZgEfC7LyHquDUpyL+NkR4OaqcBBDemwwDC4pw5cYvAK+F+ZmXiHY+6GffC3E+hAbIqBswJ84H8RjUDfgmzgfxGNyA8EJARt2AMlz4aCjD1Q1IfvaxjaoyXN2AEXE+hPcAMm6AeAzqBuwQ50M5xiDzAf2p6NnCt7KkdqHf+VnVC97WjpSHoMPC7LxDqmBlA44Is/OOqoKVDTgtzM47pR5AanXC/TfqY39Wy8DOQre4A9UKmBJmt1NBtCKVDSibs+oBpDIONNEfdvLVJNyVnZRiBZwn8Q2wazQAnFMPomhVwjUA9WzvVPMkPkObegVMIj772EUNOJMyUHFbSg04BpwAjsdH1accm8Bj4AFwH7gDfE45AOV9QZnNwP5YB+PjAcLnfwf7lLEEvAOexnoCPAOeA7/6lPFfytCA1QwDY4QTd2OEG2hHCeMeYeUQ2mLluWWOsMNngY/Ae8TXfc3MzMzMzMzMzMzMzMzMzMzMzMzMEvkDAy2wiipG/dkAAAAASUVORK5CYII=\" alt=\"shield inner eyes shape\" title=\"shield inner eyes shape preview\"> | |`sieve`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAAEL0lEQVR4nO3bS4gcRRgA4G+TqFnzMiZGD2p8IQEVDxHUgyIiogdRD3rJQVDxIIgKIioqgidvQiC+UHyBCIISDKIhJgp6SHxgRFEMBpMYTUjIa7N57G7GQ83q4saZ7ma7a+L8H/Rp/5q/q6q3p+vvGkIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBCmzECmvKfgelyFhZiBYfyJTViPrZnOrVEzMuV9Ak93ifkVn2EVVmIEF+BynIE57eNo+2/7sBPfYfOEz5mOq3EpLsGFWCRN/FyM4Xs8387TF9ajVeLYhndwrGD8G5iGs7GlYJtjuLHOTveKAQwpNwFVjnvwTMk2L9bX7ePLcQtaiFkN5FmGk0q2Oa2OE+kkxwQ0MfhwmXRbKWNfHSfSSY4JKHtVVrWgQpvN3UOmVo4JaOoqq/KI/e2Un0UXOdYBM3BIvkfgTs7CjiYTTmsyWduoZq60svf/PzQ8+OSZAFjbQI6yg9n47Seni3BEveuAL3GwYOyYPlmETXS/4ivbVsnYFj7AFwXiduOOmvvas27G59IV2GmQPsWaLjHjV/IGPCjVeR7tEPsTnsKZtfeyg+kZc8/E+1hq8tNYS7onv40VeBzXYrFUxtiDQf+c/6g0oKulwtpO/I5vpAGe0445Kn03rJLqUQfbfzuA/VPfxd72mO5X9Ne4Sypfz8fDWCdVP7u13YVfCsS1cBh31trbHjMoXYlF7+eb1F/A24t5dXa6lyxT72BWPRr/Ms61DliWKW83S5pOmGMCTsZ1GfIWcXrTCXNMwFLpO6AXNf5UmGMCzsmQs6ihphPmmIC5GXIWtavphDkmYEuFNnun/CyOb3dDef6WYwLWSQukokZxb4U8VV78ND4BuZwrlRj26P5svqLd5r0CsePHCB4oEd/CdhkeQ3MblNYEaxy/ILdSKkPAbLwmXdmdBvIH3ISLu8S1pArrRjwrbfbqK7fidamAtkH69584OMN4Abe14xfgZWmA9/wr7mc8J+1+GzcPL7WP1brXj8ba59MXFilWUBs/HsFDBeKO4SvcLf3nLFHsncD4MYpTa+x3z7hdufvzED4s2WaztEWxbD1ocY39niTXzoSynZwl3dfLOE+1ly2zK7SpLFcxrsruuCplgiolj76YgJxv4roZazJZTMBkw00miwmYrC8m4HCFNgcqtBkpGd/SB1sTqVZc+7hCm09Kxm+T9q025kSagBXSNpKiduDVkjneLRl/wrpF8YXRQbwiPbo+WaLdW9J+o7UF47fro3rQNf67HvObVJxbLq2YJ24VGcB9+EjnSup+6deQpJ8dLZfK4BulDVuHJsRuxZs4v4Z+dpXrd8LzcYP0JTkkDdgB6aepRwp+xoBU67kSV0ivOme2P2M5fuzSflDD9/sQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGE8P/2FwwqTO2jDZLdAAAAAElFTkSuQmCC\" alt=\"sieve inner eyes shape\" title=\"sieve inner eyes shape preview\"> | |`star`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAACrUlEQVR4nO3bzU4UQRiF4RcwEUjAvwWCUVfGwKiJC12gC3bu8RL0urwD78HEoHuMorhBQDBuUIxR48+4qJo0mrGn7YHvdNLnSUh3gOFUzVdV09NMgZmZmZmZmZmZmZmZmZmZmZmZmZnZoRkLzlsCrgN7wOfg7EFmgDv5uBEVeiwqKDsNPMznr4EV4AmwCqwB+0HtmAYWgGvAYv66lH92N6gNAIxEhpFG17uSn2+SCvE8n+8CO/kxb4EvFXMmgTngLHAuHy8AHWA+n/fTzb/7vmLO0KILALBOMdr+Vxf4APwCPgI/8/fHgBPAKHCS+v1aBy7XfGwt0UsQpGWnbgFGgFP5/MzhNOcPj4/gb5YajQ4krflN9TQ6UFGAZ4LMqlajAxWvAdOkdVyRXaZLeh35FBmqmAH7wLYgd5BNgp980BQA0mVm00japCrAC1FumTVFqKoAW6LcMm8UoaoC7Ihyy+wqQlUFkHR2AMmg8AwolN2jOjKqa/FJmnc7egL4Gh2qfDP0Hc29qH6+AeOKYNUSBNVvLUcIH/k9ygLIOt1HKwvQpBkga4sLkLRyBhjaAkwIs/8muQICF6BH1hYXIGnlDJB1uo/WFWCS5rwLBjiOaEaqCjAnyi0zqwh1AQqtKoCkswNIBoVnQKFVBTgvyi0jaZOqAAui3DKSNqkK0BHllpEUwB9NLLTmo4kdmvfkQ2rTfHSoogBXBJlVXY0OVBTgliCzqsXoQMX9mGE6+YO0RveOB7coTefjFPX7dXuIttXStE16GxSb9LYoNunt5POq/zocJ72xms3HOdJ1fm+T3sV/PC58k160ZVInu8BL4AFwD7hBGrlRpoCbwP3chlcH2rUc2I7wGbBE2mS3QvNG2QxpedwDHmmbYmZmZmZmZmZmZmZmZmZmZmZmZmZWy28+jGSBQsfw7QAAAABJRU5ErkJggg==\" alt=\"star inner eyes shape\" title=\"star inner eyes shape preview\"> | |`vertical_lines`| <img src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAACgklEQVR4nO3bTUtUURzH8a81boKwB3OiRRFBYSvTltEupFcQ0S7spUSLkAjxDUS9gR7eRU/uMqgIMghzIorIUZsW5w6M15y596T3jPr9wAE3vzn3nt/MdXP/IEmSJEmSJEmSJEmSJEmStGX2p74AYBA4C5wEWsDPgrmhLFcHfgPLBXPHs9wQ8B34U+Zid5M6MAt8Ixx8e70GrnfJXQSeAc2OTBN4CoxvkhkAbgBzub0awAww8n+3svNcAD6z/jDy6yFQy+VuAStdMk1gKpepAY967LUAjG3h/fW1Or0Pv72mO3JXgbUCmTVgsiN3r+BeC+yRX8IsxQ6kBawCo4T/VW9L5OazzPnsM4rmZrbxvvvCIBuf+b3WbeByyUwLuATcKZlpZNdYmX1VbgacAQ6VzIwDExF7TUTkDgOnI/aKVnUBRyIyw4SDKetoZG44IhOt6gIGIjNV5ypTdQHKsYDELCAxC0jMAhKzgMQsIDELSMwCErOAxCwgMQtIzAISs4DELCAxC0jMAhKzgMQsIDELSMwCErOAxCwgMQtIzAISq7qAVmSm6lxlqi5gKSKzSHhruayvkbnFiEy0qgt4T3g9vYwX2SrreUSuAXyI2GtHmaH4+/orwDnCsMV8idwbwpdrlHIDGve38b77xghhHKjIgdztyE1SbERpFbjSkZsuuNcn4NgW32vfGqN3CQ/YOKQ3xfrpyPxqAjdzmRph4K/X4e+ZIb22EcLjqMH6w3gJXOuSGweeEOaC25ll4DFh+vJfBgijr69yey0RHjvJvvmVDiNsokYYXTpAmJ78UjB3EDiV/f0R+FEwVwdOAL+Ad4RHliRJkiRJkiRJkiRJkiRJ0m7wF0L1IwbtR2XgAAAAAElFTkSuQmCC\" alt=\"vertical_lines inner eyes shape\" title=\"vertical_lines inner eyes shape preview\"> |
 * @member {module:model/InnerEyeShapes} shape
 */
InnerEyeStyle.prototype['shape'] = undefined;






export default InnerEyeStyle;

