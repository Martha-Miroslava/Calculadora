import java.util.Collections;
import org.apache.thrift.TException;

public class CalculadoraHandler implements Calculadora.Iface {

    @Override
    public double sumar(double numeroA, double numeroB) throws TException {
        double respuesta = numeroA +numeroB;
        return respuesta;
    }

    @Override
    public double restar(double numeroA, double numeroB) throws TException {
        double respuesta = numeroA -numeroB;
        return respuesta;
    }

    @Override
    public double multiplicar(double numeroA, double numeroB) throws TException {
        double respuesta = numeroA*numeroB;
        return respuesta;
    }

    @Override
    public double dividir(double numeroA, double numeroB) throws TException {
        double respuesta = numeroA/numeroB;
        return respuesta;
    }
}
