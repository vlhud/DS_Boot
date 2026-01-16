import sys
from config import NUM_OF_STEPS, REPORT_TEMPLATE
from analytics import Research, Calculations, Analytics

def main():
    if len(sys.argv)!=2:
        print("Error")
    else:
        path=sys.argv[1]
        research=Research(path)
        lines=research.file_reader() 
        calc=Calculations(lines)
        count=calc.counts()

        fract=calc.fractions()

        analyt=Analytics(lines)
        analyt.predict_random(NUM_OF_STEPS)
        pred=analyt.predicted_values()

        report=REPORT_TEMPLATE.format(
            total= sum(count), 
            tails= count[1], 
            heads= count[0], 
            fr_tails=fract[1], 
            fr_heads=fract[0], 
            num_steps=NUM_OF_STEPS, 
            predicted_tails= pred[1], 
            predicted_heads=pred[0]
        )
        print(report)
        analyt.save_file(report, "report", "txt")

if __name__ == "__main__":
    main()