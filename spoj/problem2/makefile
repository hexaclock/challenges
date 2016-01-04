CXX      = g++
OBJS     = prime1.o
#important.. means to build project with debug info in executable
#when submitting project for release, use -O2 or -O3 <- the "O" stands for optimize
CXXFLAGS = -g -fmessage-length=0
TARGET   = prime1

#rules for building the project
#target: dependencies
#__tab- build command
all: $(TARGET)
$(TARGET): $(OBJS)
	$(CXX) $(OBJS) -o $(TARGET)
	
clean:
	rm -f $(OBJS) $(TARGET) *~

